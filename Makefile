PYTHON = .venv/Scripts/python
UIC = .venv/Scripts/pyside6-uic
PIP = .venv/Scripts/pip
RCC = .venv/Scripts/pyside6-rcc

# Check if virtual environment exists, create it if not, and install requirements
.venv:
	python -m venv .venv
	$(PIP) install -r requirements.txt

# generate resources_rc.py file
res:
	$(RCC) resources.qrc -o resources_rc.py

# generate ui_form.py file
uic:
	$(UIC) form.ui -o ui_form.py

build: .venv res uic

# Start
start:
	$(PYTHON) main.py

# build and run
run: build start

# build and run no venv
deb_build: res uic start

# Default target
default: build