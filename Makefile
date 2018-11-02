build: todx/*
	rm -fr build/* dist/*
	python3 setup.py sdist bdist_wheel

install:
	pip3 install --force-reinstall dist/*.whl