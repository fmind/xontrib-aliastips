init:
	pip install '.[dist]'
	pip install -e .

load:
	xontrib load aliastips

wheel:
	python setup.py bdist_wheel

upload: wheel
	twine upload -r pypi dist/*.whl
