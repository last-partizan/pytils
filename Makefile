publish: build
	twine upload dist/*

build: clean
	python setup.py sdist

clean:
	rm -rf dist
