# Doc options
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
# Test options
TESTSCRIPT    ?= test.py

.PHONY: test Makefile docs-clean docs prep help

help:
	@echo "Available Options:"
	@echo "    lint: lint evertyhing in the coinmetrics directory."
	@echo "    docs: build the RST documentation for RTD."
	@echo "    docs-clean: wipe docs clean."
	@echo "    test: execute unit test in \`$(TESTSCRIPT)\`"

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
