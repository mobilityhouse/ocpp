.PHONY: help .install-poetry update install docs tests build deploy

.DEFAULT_GOAL := help

IS_POETRY := $(shell pip freeze | grep "poetry==")
IS_TWINE := $(shell pip freeze | grep "twine==")


help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  help           outputs this helper"
	@echo "  build          builds the project .whl with poetry"
	@echo "  update         updates the dependencies in poetry.lock"
	@echo "  install        installs the dependencies in the env"
	@echo "  test           run all the tests and linting"
	@echo "  deploy         deploys the project using twine (not recommended, only use if really needed)"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."


export PATH := ${HOME}/.local/bin:$(PATH)

.install-poetry:
	@if [ -z ${IS_POETRY} ]; then pip install poetry; fi

update: .install-poetry
	poetry update

install: .install-poetry
	poetry install

docs: .install-poetry
	poetry run sphinx-build -b html docs/source docs/build

tests: .install-poetry
	poetry run flake8 ocpp tests
	poetry run py.test -vvv --cov=ocpp --cov-report=term-missing tests/

build: .install-poetry
	poetry build

deploy: install
	@if [ -z ${IS_TWINE} ]; then pip install twine; fi
	twine upload dist/*.tar.gz
