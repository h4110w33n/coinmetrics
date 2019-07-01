# Doc options
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
# Test options
TESTSCRIPT    ?= test.py
LEGTESTSCRIPT ?= test-legacy.py

.PHONY: help lint docs clean-docs test test-legacy clean-build clean-pyc clean dist release install

help:
	@echo "Available Options:"
	@echo "    lint: lint evertyhing in the coinmetrics directory."
	@echo "    docs: build the RST documentation for RTD."
	@echo "    clean-docs: wipe docs clean."
	@echo "    test: execute unit test in \`$(TESTSCRIPT)\`."
	@echo "    test-legacy: execute unit test in \`$(LEGTESTSCRIPT)\`."
	@echo "    dist: install install the \`coinmetrics\` package to the local environment."
	@echo "    dist: build the \`coinmetrics\` package (no upload)"	
	@echo "    release: build the \`coinmetrics\` package then upload to PyPi."
	@echo "    clean-build: remove all build artifacts/eggs."
	@echo "    clean-pyc: remove all caches/pyc's"
	@echo "    clean: execute all clean actions: clean-build, clean-pyc and clean-docs."

lint:
	pylint coinmetrics/*.py

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

clean: clean-build clean-pyc clean-docs

dist: test docs clean
	python setup.py sdist
	python setup.py bdist_wheel

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

install: clean
	python setup.py install
