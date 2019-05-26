.PHONY: deps test build deploy

export PATH := ${HOME}/.local/bin:$(PATH)

deps:
	pip3 install --user -r requirements_dev.txt

test:
	flake8 ocpp tests
	py.test -vvv --cov=ocpp --cov-report=term-missing tests/

build:
	rm -Rf dist  ocpp.egg-info
	MAKE_RELEASE=1 python3 setup.py sdist

deploy: deps
	twine upload dist/*.tar.gz

