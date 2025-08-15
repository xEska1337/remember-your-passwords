import json
from pathlib import Path
from typing import Dict, List, TypedDict, Optional, Any
from datetime import datetime


class Settings:
    def __init__(self, settings_dict: Dict[str, bool]):
        self.start_on_login = settings_dict.get("start_on_login", False)
        self.close_to_tray = settings_dict.get("close_to_tray", True)
        self.start_minimized = settings_dict.get("start_minimized", False)

    def to_dict(self) -> Dict[str, bool]:
        return {
            "start_on_login": self.start_on_login,
            "close_to_tray": self.close_to_tray,
            "start_minimized": self.start_minimized
        }

class SaveData(TypedDict):
    password: str
    hint: str
    reminder_type: str
    reminder_time: str
    correct_attempts: int
    wrong_attempts: int
    last_attempt: str

class SaveManager:
    def __init__(self, file_path: str = "savedPasswords.json"):
        self.file_path = Path(file_path)
        self.data = self._load_data()
        if "settings" not in self.data:
            self.data["settings"] = {
                "start_on_login": False,
                "close_to_tray": True,
                "start_minimized": False
            }
            self._save_data()
        if "passwords" not in self.data:
            self.data["passwords"] = {}
            self._save_data()

        self._settings_obj = Settings(self.data["settings"])

    def _load_data(self) -> Dict[str, Any]:
        if self.file_path.exists() and not self.file_path.stat().st_size == 0:
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def _save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    @property
    def settings(self) -> Settings:
        return self._settings_obj

    def update_settings(self, **kwargs) -> Settings:
        for key, value in kwargs.items():
            if hasattr(self._settings_obj, key):
                setattr(self._settings_obj, key, value)
        self.data["settings"] = self._settings_obj.to_dict()
        self._save_data()
        return self._settings_obj

    def get_setting(self, key: str, default: Any = None) -> Any:
        if hasattr(self._settings_obj, key):
            return getattr(self._settings_obj, key)
        return default

    @property
    def passwords(self) -> Dict[str, SaveData]:
        return self.data["passwords"]

    def add_password(self, name: str, data: SaveData):
        self.passwords[name] = data
        self._save_data()

    def get_password(self, name: str) -> Optional[SaveData]:
        return self.passwords.get(name)

    def list_passwords(self) -> List[str]:
        return list(self.passwords.keys())

    def delete_password(self, name: str):
        if name in self.passwords:
            del self.passwords[name]
            self._save_data()

    def update_correct_attempt(self, name: str) -> bool:
        if name in self.passwords:
            self.passwords[name]['correct_attempts'] += 1
            self.passwords[name]['last_attempt'] = datetime.now().isoformat()
            self._save_data()
            return True
        return False

    def update_wrong_attempt(self, name: str) -> bool:
        if name in self.passwords:
            self.passwords[name]['wrong_attempts'] += 1
            self.passwords[name]['last_attempt'] = datetime.now().isoformat()
            self._save_data()
            return True
        return False

    def update_password(self, name: str, data: SaveData):
        if name in self.passwords:
            self.passwords[name] = data
            self._save_data()