.PHONY: help .check-pypi-envs .install-poetry update install docs tests build deploy

.DEFAULT_GOAL := help

export PATH := ${HOME}/.local/bin:$(PATH)

IS_POETRY := $(shell pip freeze | grep "poetry==")

CURRENT_VERSION := $(shell poetry version -s)

help:
	@echo "Please use 'make <target>', where <target> is one of"
	@echo ""
	@echo "  build                            builds the project .whl with poetry"
	@echo "  deploy                           deploys the project using poetry (not recommended, only use if really needed)"
	@echo "  help                             outputs this helper"
	@echo "  install                          installs the dependencies in the env"
	@echo "  release version=<sem. version>   bumps the project version to <sem. version>, using poetry;"
	@echo "                                   Updates also docs/source/conf.py version;"
	@echo "                                   If no version is provided, poetry outputs the current project version"
	@echo "  test                             run all the tests and linting"
	@echo "  update                           updates the dependencies in poetry.lock"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."


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

release: .install-poetry
	@echo "Please remember to update the CHANGELOG.md, before tagging the release"
	@sed -i ".bkp" "s/release = '${CURRENT_VERSION}'/release = '${version}'/g" docs/source/conf.py
	@poetry version ${version}

deploy: update tests
	poetry publish --build
