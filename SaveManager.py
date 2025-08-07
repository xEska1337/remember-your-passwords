import json
from pathlib import Path
from typing import Dict, List, TypedDict, Optional
from datetime import datetime


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
        self.passwords: Dict[str, SaveData] = self._load_data()

    def _load_data(self) -> Dict[str, SaveData]:
        if self.file_path.exists():
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def _save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.passwords, file, indent=4)

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