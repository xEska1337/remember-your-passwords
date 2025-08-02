PYTHON = .venv/Scripts/python
UIC = .venv/Scripts/pyside6-uic
UI_FILE = form.ui
PY_FILE = ui_form.py

# Check if virtual environment exists, create it if not, and install requirements
.venv:
	python -m venv .venv
	.venv/Scripts/pip install -r requirements.txt

# venv and generate the ui_form.py file
build: .venv
	$(UIC) $(UI_FILE) -o $(PY_FILE)

# build and run
run: build
	$(PYTHON) main.py

# new ui and run
ui:
	$(UIC) $(UI_FILE) -o $(PY_FILE)
	$(PYTHON) main.py

# Start
start:
	$(PYTHON) main.py

# Default target
default: build
