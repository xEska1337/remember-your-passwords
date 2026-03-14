from __future__ import annotations
import asyncio
from datetime import datetime, timedelta
from threading import Event, Thread, Lock, Timer
from typing import Dict, Optional
from desktop_notifier import DesktopNotifier, DEFAULT_SOUND


class NotificationService:
    def __init__(self, app_name: str = "Remember Your Passwords"):
        self._app_name = app_name
        self._app_start_time = datetime.now()

        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._loop_thread: Optional[Thread] = None
        self._notifier = None
        self._loop_ready = Event()

        self._jobs: Dict[str, Timer] = {}
        self._jobs_lock = Lock()
        self._stopping = Event()


    def start(self) -> None:
        if self._loop_thread and self._loop_thread.is_alive():
            return

        self._stopping.clear()
        self._loop_thread = Thread(target=self._run_loop_thread, name="NotificationLoop", daemon=True)
        self._loop_thread.start()
        self._loop_ready.wait(timeout=5.0)


    def stop(self) -> None:
        self._stopping.set()
        with self._jobs_lock:
            for t in self._jobs.values():
                try:
                    t.cancel()
                except Exception:
                    pass
            self._jobs.clear()

        loop = self._loop
        if loop:
            def _stop():
                try:
                    loop.stop()
                except Exception:
                    pass

            loop.call_soon_threadsafe(_stop)

        if self._loop_thread and self._loop_thread.is_alive():
            self._loop_thread.join(timeout=5.0)

        self._loop = None
        self._loop_thread = None
        self._notifier = None


    def schedule_for(self, name: str, reminder_type: str, reminder_time_hhmm: str) -> None:
        self.unschedule(name)

        if self._stopping.is_set():
            return
        if reminder_type == "none":
            return

        if reminder_type == "after_start":
            self._schedule_after_start(name, reminder_time_hhmm)
            return

        try:
            next_dt = self._compute_next_run(reminder_type, reminder_time_hhmm, base=datetime.now())
        except Exception:
            next_dt = datetime.now() + timedelta(minutes=1)

        delay = max(0.0, (next_dt - datetime.now()).total_seconds())

        def _fire():
            if self._stopping.is_set():
                return
            self.notify(
                title=f"Password Practice: {name}",
                message="Time to practice your password."
            )
            try:
                nxt = self._compute_next_run(reminder_type, reminder_time_hhmm, base=datetime.now())
                nxt_delay = max(0.0, (nxt - datetime.now()).total_seconds())
            except Exception:
                nxt_delay = 60.0
            with self._jobs_lock:
                if not self._stopping.is_set():
                    t2 = Timer(nxt_delay, _fire)
                    self._jobs[name] = t2
                    t2.daemon = True
                    t2.start()

        t = Timer(delay, _fire)
        t.daemon = True
        with self._jobs_lock:
            self._jobs[name] = t
        t.start()

    def _schedule_after_start(self, name: str, duration_hhmm: str) -> None:
        try:
            h, m = self._parse_hhmm(duration_hhmm)
            target_time = self._app_start_time + timedelta(hours=h, minutes=m)

            delay = (target_time - datetime.now()).total_seconds()

            if delay <= 0:
                return

            def _fire_once():
                if self._stopping.is_set():
                    return
                self.notify(
                    title=f"Password Practice: {name}",
                    message="Time to practice your password."
                )

            t = Timer(delay, _fire_once)
            t.daemon = True
            with self._jobs_lock:
                self._jobs[name] = t
            t.start()

        except Exception:
            pass


    def unschedule(self, name: str) -> None:
        with self._jobs_lock:
            t = self._jobs.pop(name, None)
        if t:
            try:
                t.cancel()
            except Exception:
                pass


    def notify(self, title: str, message: str) -> None:
        loop = self._loop
        notifier = self._notifier

        if not loop or not notifier:
            return

        async def _send():
            try:
                await notifier.send(title=title, message=message, sound=DEFAULT_SOUND)
            except Exception:
                pass

        try:
            asyncio.run_coroutine_threadsafe(_send(), loop)
        except Exception:
            pass



    def _run_loop_thread(self) -> None:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop = loop

            try:
                self._notifier = DesktopNotifier(app_name=self._app_name)
            except Exception:
                self._notifier = None

            self._loop_ready.set()

            loop.run_forever()
        finally:
            try:
                loop = self._loop
                if loop and not loop.is_closed():
                    pending = asyncio.all_tasks(loop=loop)
                    for task in pending:
                        task.cancel()
                    try:
                        loop.run_until_complete(asyncio.sleep(0))
                    except Exception:
                        pass
                    loop.close()
            except Exception:
                pass



    @staticmethod
    def _compute_next_run(reminder_type: str, hhmm: str, base: datetime) -> datetime:
        hour, minute = NotificationService._parse_hhmm(hhmm)
        candidate = base.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if reminder_type == "daily":
            if candidate <= base:
                candidate += timedelta(days=1)
            return candidate

        if reminder_type == "weekly":
            if candidate <= base:
                candidate += timedelta(days=7)
            return candidate

        if reminder_type == "monthly":
            if candidate <= base:
                year = candidate.year
                month = candidate.month + 1
                if month > 12:
                    year += 1
                    month = 1
                day = candidate.day
            else:
                year = candidate.year
                month = candidate.month
                day = candidate.day

            day = min(day, NotificationService._days_in_month(year, month))
            return candidate.replace(year=year, month=month, day=day)

        return base + timedelta(minutes=1)


    @staticmethod
    def _days_in_month(year: int, month: int) -> int:
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        this_month = datetime(year, month, 1)
        return (next_month - this_month).days


    @staticmethod
    def _parse_hhmm(hhmm: str) -> tuple[int, int]:
        parts = hhmm.split(":")
        if len(parts) != 2:
            raise ValueError("Invalid HH:MM")
        h = int(parts[0])
        m = int(parts[1])
        if not (0 <= h < 24) or not (0 <= m < 60):
            raise ValueError("Invalid time")
        return h, m