# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = docs/build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

make install:
	rm -f dist/*.tar.gz
	rm -f build/lib/GenericSimulationLibrary/*.py
	rm -f /miniconda3/lib/python3.7/site-packages/GenericSimulationLibrary/*.py
	python setup.py install

version:
	nano GenericSimulationLibrary/version_file.py

test.pypi:
	rm -f dist/*.tar.gz
	python setup.py sdist
	python -m twine upload --repository testpypi dist/*

pypi:
	rm -f dist/*.tar.gz
	python setup.py sdist
	python -m twine upload --repository pypi dist/*

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
