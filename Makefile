install:
	pip install -e "$(shell pwd)"
	jupyter nbextension install vendor/facets/facets-dist

.PHONY: install
