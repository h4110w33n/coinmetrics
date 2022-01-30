# Doc options
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
# Test options
TESTSCRIPT    ?= test.py
LEGTESTSCRIPT ?= test-legacy.py
TESTCSV		  ?= test.csv

.PHONY: help lint docs clean-docs test test-legacy clean-build clean-pyc clean dist release install

help:
	@echo "Available Options:"
	@echo "    lint: lint evertyhing in the coinmetrics directory."
	@echo "    lint-extras: lint all the other Python files in this repo."
	@echo "    docs: build the RST documentation for RTD."
	@echo "    clean-docs: wipe docs clean."
	@echo "    test: execute unit test in \`$(TESTSCRIPT)\`."
	@echo "    test-legacy: execute unit test in \`$(LEGTESTSCRIPT)\`."
	@echo "    dist: build the \`coinmetrics\` package (no upload)"	
	@echo "    release: build the \`coinmetrics\` package then upload to PyPi."
	@echo "    clean-build: remove all build artifacts/eggs."
	@echo "    clean-pyc: remove all caches/pyc's"
	@echo "    clean: execute all clean actions: clean-build, clean-pyc and clean-docs."
	@echo "    coverage: generate a report of functions exercised by test.py"

lint:
	pylint coinmetrics/*.py

lint-extras:
	pylint test.py

black:
	black coinmetrics/*.py
	black test.py

docs:
	@mkdir -p "$(BUILDDIR)"
	@mkdir -p {"$(BUILDDIR)/doctrees","$(BUILDDIR)/html"}
	$(SPHINXBUILD) -M "html" "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -v

clean-docs:
	@rm -rf "$(BUILDDIR)"

test:
	python3 $(TESTSCRIPT) || python $(TESTSCRIPT)

test-legacy:
	python3 $(LEGTESTSCRIPT) || python $(LEGTESTSCRIPT)

clean-test:
	rm -f $(TESTCSV)

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

coverage:
	coverage run $(TESTSCRIPT)
	coverage report --include="coinmetrics/*" -m

coverage-upload: coverage
	codecov

clean: clean-build clean-pyc clean-docs clean-test

dist: test clean
	python setup.py sdist
	python setup.py bdist_wheel

release: clean
	python setup.py sdist
	python setup.py bdist_wheel
	pip install twine
	twine upload dist/*

install: clean
	python setup.py install
