install:
	python -m pipenv install --dev

linting:
	pipenv run flake8

unit:
	PYTHONPATH=./src pipenv run pytest tests

run:
	PYTHONPATH=./src pipenv run python src/main.py
