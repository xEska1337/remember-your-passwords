<h1 align="center">Remember Your Passwords</h1>

---

# :page_facing_up: Project Description

Remember Your Passwords is a secure, desktop-based application designed to help you practice and memorize your passwords using Spaced Repetition. 

Stop forgetting your passwords and start remembering them actively!

---

## :sparkles: Features

- **Secure Storage**: Passwords are hashed using **Argon2** (the winner of the Password Hashing Competition). The application verifies your input without ever storing the plain-text password.
- **Smart Reminders**: Schedule practice sessions to ensure long-term retention:
  - Daily, Weekly, or Monthly reminders.
  - "After Start" reminders (e.g., practice 10 minutes after login).
- **Success Tracking**: Track your correct and incorrect attempts and view your success rate over time.
- **System Tray Integration**: runs quietly in the background; minimize to tray to keep your taskbar clean.
- **Autostart**: Option to automatically launch with Windows/Linux.
- **Privacy First**: All data is stored locally in `savedPasswords.json`.

---

## :hammer: Installation
#### :pushpin:Requirements
- Python 3
- pip
1. Clone the repository
   ```
   git clone https://github.com/xEska1337/remember-your-passwords
   ```
2. Move to repository
   ```
   cd imageTagger
   ```
3. Install and run\
   **Note:** If you have make installed, you can simply run `make run` to set up the environment and launch the app.\
   **Windows:** Double-click the run.bat file. It will automatically set up the environment, install dependencies, and launch the app.\
   **Linux:** Run the following commands in your terminal:
   1. Create venv and activate it
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
    2. Install dependencies
    ```
    pip install -r requirements.txt
    ```
   3. Compile Resources (Qt)
   ```
   pyside6-rcc resources.qrc -o resources_rc.py
   pyside6-uic form.ui -o ui_form.py
   ```
    4. Run the application
    ```
    python main.py
    ```
---

## :hammer_and_wrench: Built With

* **Python 3**
* **PySide6 (Qt)** - GUI Framework
* **Argon2-cffi** - Secure Password Hashing
* **Desktop-Notifier** - Cross-platform System Notifications

---

##  :fire: Contribution

Your contributions are always welcome and appreciated. Following are the things you can do to contribute to this project.

1. **Report a bug** <br>
If you think you have encountered a bug, and I should know about it, feel free to report it [here](https://github.com/xEska1337/remember-your-passwords/issues) and I will take care of it.

2. **Request a feature** <br>
You can also request for a feature [here](https://github.com/xEska1337/remember-your-passwords/discussions), and if it will viable, it will be picked for development.  

3. **Create a pull request** <br>
It can't get better then this, your pull request will be appreciated by the community. You can get started by picking up any open issues from [here](https://github.com/xEska1337/remember-your-passwords/issues) and make a pull request.
