# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Raincoat
SOURCEDIR     = .
BUILDDIR      = _build
PORT = 8001

# Put it first so that "make" without argument is like "make help".
help:
	. $(VENV); $(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	-rm -rf _build/*

run:
	sphinx-autobuild $(ALLSPHINXOPTS) . -a _build/html --host 0.0.0.0 --port $(PORT)

spelling:
	$(SPHINXBUILD) -b spelling $(ALLSPHINXOPTS) . _build/spelling

open:
	open _build/html/index.html


.PHONY: help install clean run Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
