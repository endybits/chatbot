install:
	python -m pip install -U pip && \
	pip install -r requirements.txt
	export PYTHONPATH=.
lint:
	pylint --disable=R,C app *.py
tests:
	python -m pytest -vv --cov=app
format:
	black *.py app/*.py

all: install lint tests format