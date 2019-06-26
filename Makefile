# Doc options
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
# Test options
TESTSCRIPT    ?= test.py
LEGTESTSCRIPT ?= test-legacy.py

.PHONY: test test-legacy Makefile docs-clean docs prep help clean-pyc clean-build

help:
	@echo "Available Options:"
	@echo "    lint: lint evertyhing in the coinmetrics directory."
	@echo "    docs: build the RST documentation for RTD."
	@echo "    docs-clean: wipe docs clean."
	@echo "    test: execute unit test in \`$(TESTSCRIPT)\`"
	@echo "    release: test then upload our library."	

lint:
	pylint coinmetrics/*.py

prep:
	mkdir -p "$(BUILDDIR)"

docs: prep Makefile
	@mkdir -p {"$(BUILDDIR)/doctrees","$(BUILDDIR)/html"}
	$(SPHINXBUILD) -M "html" "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -v

docs-clean: Makefile
	@rm -rf "$(BUILDDIR)"

test: Makefile
	python3 $(TESTSCRIPT) || python $(TESTSCRIPT)

test-legacy: Makefile
	python3 $(LEGTESTSCRIPT) || python $(LEGTESTSCRIPT)

release:
	python setup.py sdist bdist_wheel

clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} \;
	find . -name '*.pyo' -exec rm -rf {} \;

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clean: clean-pyc clean-build docs-clean
	@echo All Clean