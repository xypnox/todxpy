build: todx/* setup.py
	rm -fr build/* dist/*
	python3 setup.py sdist bdist_wheel

install:
	pip3 install --force-reinstall dist/*.whl --user

install-travis:
	pip3 install --force-reinstall dist/*.whl

publish:
	twine upload dist/*

docs:
	pycco todx/*.py