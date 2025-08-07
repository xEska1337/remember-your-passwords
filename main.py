import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QListWidget
from SaveManager import SaveManager, SaveData
from datetime import datetime
from argon2 import PasswordHasher

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Main

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.save_manager = SaveManager()

        self.ph = PasswordHasher()

        self.refresh_password_list()

        # Add button
        self.ui.addButton.clicked.connect(self.show_add_password_page)
        # Go back to the main page button
        self.ui.addPasswordCancelButton.clicked.connect(self.show_main_page)
        # Add a password button
        self.ui.addPasswordConfirmButton.clicked.connect(self.add_password)
        # Remove a password button
        self.ui.removeButton.clicked.connect(self.remove_password)
        # Show password on a right panel
        self.ui.passwordsList.itemClicked.connect(self.show_password)
        # Hint button
        self.ui.hintButton.clicked.connect(self.show_hint)
        # Submit password button
        self.ui.submitPasswordButton.clicked.connect(self.check_password)
        # Edit password button
        self.ui.currentPasswordSettingsButton.clicked.connect(self.show_edit_page)
        # Cancel edit password button
        self.ui.editCancelButton.clicked.connect(self.show_password)
        # Confirm edit password button
        self.ui.editConfirmButton.clicked.connect(self.edit_password)


    def show_add_password_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.addPasswordInput.clear()
        self.ui.addPasswordInputConfirm.clear()
        self.ui.addPasswordHint.clear()
        self.ui.addPasswordRadioButtonNoReminders.setChecked(True)
        self.ui.addPasswordRemiderTime.setTime(datetime.now().time())


    def show_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def refresh_password_list(self):
        self.ui.passwordsList.clear()
        self.ui.passwordsList.addItems(self.save_manager.list_passwords())
        self.ui.rightColumn.setCurrentIndex(1)


    def add_password(self):
        password = self.ui.addPasswordInput.text()
        confirm_password = self.ui.addPasswordInputConfirm.text()

        if not password:
            QMessageBox.warning(self, "Error", "Password cannot be empty.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        reminder_type = "none"
        if self.ui.addPasswordRadioButtonEveryday.isChecked():
            reminder_type = "daily"
        elif self.ui.addPasswordRadioButtonWeek.isChecked():
            reminder_type = "weekly"
        elif self.ui.addPasswordRadioButtonMonth.isChecked():
            reminder_type = "monthly"

        password_data: SaveData = {
            "password": self.ph.hash(password),
            "hint": self.ui.addPasswordHint.toPlainText(),
            "reminder_type": reminder_type,
            "reminder_time": self.ui.addPasswordRemiderTime.time().toString("HH:mm"),
            "correct_attempts": 0,
            "wrong_attempts": 0,
            "last_attempt": datetime.now().isoformat()
        }

        name, ok = QInputDialog.getText(self, "Add Password", "Enter a name for the password:")
        if ok and name:
            if name in self.save_manager.list_passwords():
                QMessageBox.warning(self, "Error", "Password with this name already exists.")
                return
            self.save_manager.add_password(name, password_data)
            self.refresh_password_list()
            self.show_main_page()


    def remove_password(self):
        if not self.ui.passwordsList.currentItem():
            QMessageBox.warning(self, "Error", "No password selected.")
            return
        name = self.ui.passwordsList.currentItem().text()
        check = QMessageBox.question(self, "Remove Password", f"Are you sure you want to remove '{name}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if check == QMessageBox.StandardButton.Yes:
            self.save_manager.delete_password(name)
            self.refresh_password_list()


    def show_password(self):
        if not self.ui.passwordsList.currentItem():
            return

        self.ui.rightColumn.setCurrentIndex(0)

        name = self.ui.passwordsList.currentItem().text()
        password_data = self.save_manager.get_password(name)

        if password_data:
            self.ui.correctLabel.setText("Correct: " + str(password_data["correct_attempts"]))
            self.ui.wrongLabel.setText("Wrong: " + str(password_data["wrong_attempts"]))
            if password_data["correct_attempts"] + password_data["wrong_attempts"] != 0:
                self.ui.successRateLabel.setText("Success rate: " + str(f"{password_data['correct_attempts'] / (password_data['correct_attempts'] + password_data['wrong_attempts']) * 100:.2f}%"))
            else:
                self.ui.successRateLabel.setText("Success rate:")

            dt = datetime.fromisoformat(password_data["last_attempt"])
            self.ui.lastAttemptLabel.setText("Last attempt: " + dt.strftime('%d %b %Y %H:%M:%S'))

            if password_data["reminder_type"] != "none":
                self.ui.reminderLabel.setText("Reminder: " + str(password_data["reminder_type"]) + " at " + str(password_data["reminder_time"]))
            else:
                self.ui.reminderLabel.setText("Reminder: none")


    def show_hint(self):
        if not self.ui.passwordsList.currentItem():
            QMessageBox.warning(self, "Error", "No password selected.")
            return

        name = self.ui.passwordsList.currentItem().text()
        password_data = self.save_manager.get_password(name)

        if password_data:
            if not password_data["hint"]:
                QMessageBox.information(self, "Hint", "No hint available.")
            else:
                QMessageBox.information(self, "Hint", password_data["hint"])


    def check_password(self):
        if not self.ui.passwordEnter.text():
            QMessageBox.warning(self, "Error", "Password cannot be empty.")
            return

        password_input = self.ui.passwordEnter.text()
        password_data = self.save_manager.get_password(self.ui.passwordsList.currentItem().text())

        try:
            if self.ph.verify(password_data["password"], password_input):
                self.save_manager.update_correct_attempt(self.ui.passwordsList.currentItem().text())
                QMessageBox.information(self, "Success", "Password correct.")
                self.show_password()
        except:
            self.save_manager.update_wrong_attempt(self.ui.passwordsList.currentItem().text())
            QMessageBox.warning(self, "Error", "Password incorrect.")
            self.show_password()


    def show_edit_page(self):
        self.ui.rightColumn.setCurrentIndex(2)

        name = self.ui.passwordsList.currentItem().text()
        password_data = self.save_manager.get_password(name)

        self.ui.editHint.setPlainText(password_data["hint"])
        self.ui.editTime.setTime(datetime.strptime(password_data["reminder_time"], "%H:%M").time())

        if password_data["reminder_type"] == "none":
            self.ui.editReminderNoReminders.setChecked(True)
        elif password_data["reminder_type"] == "daily":
            self.ui.editReminderEveryday.setChecked(True)
        elif password_data["reminder_type"] == "weekly":
            self.ui.editReminderWeek.setChecked(True)
        elif password_data["reminder_type"] == "monthly":
            self.ui.editReminderMonth.setChecked(True)


    def edit_password(self):
        name = self.ui.passwordsList.currentItem().text()
        password_data = self.save_manager.get_password(name)

        password_data["hint"] = self.ui.editHint.toPlainText()

        reminder_type_edit = "none"
        if self.ui.editReminderEveryday.isChecked():
            reminder_type_edit = "daily"
        elif self.ui.editReminderWeek.isChecked():
            reminder_type_edit = "weekly"
        elif self.ui.editReminderMonth.isChecked():
            reminder_type_edit = "monthly"

        password_data["reminder_type"] = reminder_type_edit
        password_data["reminder_time"] = self.ui.editTime.time().toString("HH:mm")

        self.save_manager.add_password(name, password_data)
        self.show_password()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
