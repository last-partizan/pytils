check: build
	twine check

publish: build
	twine upload dist/*

build: clean
	python -m build

clean:
	rm -rf dist
