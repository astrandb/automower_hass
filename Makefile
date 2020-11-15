__VERSION__ = "0.5.0"

lint:
	isort custom_components
	black custom_components
	flake8 custom_components

bump:
	bump2version --allow-dirty patch Makefile custom_components/automower/const.py

bump_minor:
	bump2version --allow-dirty minor Makefile custom_components/automower/const.py

install_dev:
	pip install -r requirements-dev.txt
