.PHONY: deps test build deploy

export PATH := ${HOME}/.local/bin:$(PATH)

deps:
	pip install poetry
	poetry install

test:
	poetry run flake8 ocpp tests
	poetry run py.test -vvv --cov=ocpp --cov-report=term-missing tests/

build:
	poetry build

deploy: deps
	twine upload dist/*.tar.gz

