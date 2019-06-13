# Doc options
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
# Test options
TESTSCRIPT    ?= test.py

help:
	echo "Options: docs"

.PHONY: test help Makefile docs-clean docs prep

prep:
	mkdir -p "$(BUILDDIR)"

docs: prep Makefile
	@mkdir -p {"$(BUILDDIR)/doctrees","$(BUILDDIR)/html"}
	$(SPHINXBUILD) -M "html" "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -v

docs-clean: Makefile
	@rm -rf "$(BUILDDIR)"

test: Makefile
	python $(TESTSCRIPT)