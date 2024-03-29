clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build


format:
	black -l 88 **/*.py

install:
	pip3 install .

installdev:
	pip3 install -e .['dev']

uninstall:
	pip3 uninstall arquivos_base_criar_pacote_python
	