
all: build dist

build:
	pipenv run python setup.py sdist bdist_wheel

dist:
	pipenv run twine upload dist/*

setup:
	pipenv run pip install --upgrade twine setuptools wheel
