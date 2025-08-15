import os
import sys
import subprocess
from pathlib import Path
import ctypes
from abc import ABC, abstractmethod


class AutostartManager(ABC):
    def __init__(self, app_name: str, base_path: Path | None = None):
        self.app_name = app_name
        self.base_path = base_path or Path(__file__).resolve().parent
        self.python_path = sys.executable
        self.script_to_run = "main.py"

    @abstractmethod
    def enable(self) -> None:
        ...

    @abstractmethod
    def disable(self) -> None:
        ...

    @abstractmethod
    def is_enabled(self) -> bool:
        ...


class WindowsAutostart(AutostartManager):
    EXIT_CODE_UAC_CANCEL = 1223

    def __init__(self, app_name: str, base_path: Path | None = None):
        super().__init__(app_name, base_path)
        pythonw_path = Path(self.python_path).with_name("pythonw.exe")
        if pythonw_path.exists():
            self.python_path = str(pythonw_path)

    @staticmethod
    def _is_user_admin() -> bool:
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except Exception:
            return False

    @staticmethod
    def _relaunch_as_admin():
        params = " ".join(f'"{arg}"' for arg in sys.argv)
        try:
            result = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

            if result <= 32:
                raise RuntimeError(f"ShellExecuteW failed with code {result}")

        except OSError as e:
            if e.winerror == WindowsAutostart.EXIT_CODE_UAC_CANCEL:
                sys.exit(WindowsAutostart.EXIT_CODE_UAC_CANCEL)
            raise RuntimeError(f"Failed to trigger elevation: {e!r}")
        except Exception as e:
            raise RuntimeError(f"Failed to trigger elevation: {e!r}")
        sys.exit(0)

    def is_enabled(self) -> bool:
        try:
            result = subprocess.run(
                ["schtasks", "/query", "/tn", self.app_name],
                capture_output=True,
                text=True,
                check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            raise RuntimeError("schtasks.exe not found. This feature requires Windows Task Scheduler.")

    def disable(self) -> None:
        if self.is_enabled():
            if not self._is_user_admin():
                self._relaunch_as_admin()
            ps_command = f"Unregister-ScheduledTask -TaskName '{self.app_name}' -Confirm:$false"
            res = subprocess.run(
                ["powershell", "-NoProfile", "-Command", ps_command],
                capture_output=True, text=True, check=False
            )
            if res.returncode != 0:
                raise RuntimeError(f"Failed to disable autostart task: {res.stderr}")

    def enable(self) -> None:
        python_path = self.python_path
        script_to_run = self.script_to_run
        base_path = self.base_path

        if not Path(python_path).exists():
            raise FileNotFoundError(f"Python interpreter not found: {python_path}")
        if not Path(base_path / script_to_run).exists():
            raise FileNotFoundError(f"Script to run not found: {script_to_run}")

        if not self._is_user_admin():
            self._relaunch_as_admin()

        ps_command = f"""
                $action = New-ScheduledTaskAction -Execute '{python_path}' -Argument '{script_to_run}' -WorkingDirectory '{base_path}'
                $trigger = New-ScheduledTaskTrigger -AtLogOn
                Register-ScheduledTask -TaskName '{self.app_name}' -Action $action -Trigger $trigger -Force | Out-Null
                """

        res = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_command],
            capture_output=True, text=True, check=False
        )

        if res.returncode != 0:
            raise RuntimeError(
                "Failed to create/update scheduled task.\n"
                f"Exit code: {res.returncode}\n"
                f"Stdout: {res.stdout}\nStderr: {res.stderr}\n"
            )


class LinuxAutostart(AutostartManager):
    def _autostart_dir(self) -> Path:
        xdg_config_home = os.environ.get("XDG_CONFIG_HOME")
        if xdg_config_home:
            return Path(xdg_config_home) / "autostart"
        return Path.home() / ".config" / "autostart"

    def _desktop_file(self) -> Path:
        safe_name = "".join(c for c in self.app_name if c.isalnum() or c in (" ", "-", "_")).strip()
        safe_name = safe_name.replace(" ", "-")
        return self._autostart_dir() / f"{safe_name}.desktop"

    def is_enabled(self) -> bool:
        return self._desktop_file().exists()

    def disable(self) -> None:
        try:
            self._desktop_file().unlink(missing_ok=True)
        except Exception as e:
            raise RuntimeError(f"Failed to remove autostart entry: {e!r}")

    def enable(self) -> None:
        py = self.python_path
        script = self.base_path / self.script_to_run

        if not Path(py).exists():
            raise FileNotFoundError(f"Python interpreter not found: {py}")
        if not script.exists():
            raise FileNotFoundError(f"Script to run not found: {script}")

        autostart_dir = self._autostart_dir()
        autostart_dir.mkdir(parents=True, exist_ok=True)

        icon_path = self.base_path / "resources" / "icons" / "brain-keyhole.svg"
        icon_line = f"Icon={icon_path.resolve()}\n" if icon_path.exists() else ""

        desktop_path = self._desktop_file()
        contents = f"""[Desktop Entry]
Type=Application
Version=1.0
Name={self.app_name}
{icon_line}Exec="{py}" "{script.resolve()}"
X-GNOME-Autostart-enabled=true
X-KDE-autostart-after=panel
Terminal=false
"""

        try:
            desktop_path.write_text(contents, encoding="utf-8")
        except Exception as e:
            raise RuntimeError(f"Failed to write autostart entry: {e!r}")

def _select_system(app_name: str) -> AutostartManager:
    base_path = Path(__file__).resolve().parent
    if sys.platform.startswith("win"):
        return WindowsAutostart(app_name, base_path=base_path)
    elif sys.platform.startswith("linux"):
        return LinuxAutostart(app_name, base_path=base_path)
    else:
        raise NotImplementedError(f"Autostart not implemented for platform: {sys.platform}")


def autostart_enable(app_name: str) -> None:
    _select_system(app_name).enable()


def autostart_disable(app_name: str) -> None:
    _select_system(app_name).disable()


def autostart_is_enabled(app_name: str) -> bool:
    return _select_system(app_name).is_enabled()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python Autostart.py [--enable|--disable] <AppName>")
        sys.exit(1)

    action = sys.argv[1]
    app_name = sys.argv[2]

    if action == "--enable":
        autostart_enable(app_name)
    elif action == "--disable":
        autostart_disable(app_name)
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)