install:
	pip install requests

test:
	python -m unittest discover -s . -p 'test_*.py'

run:
	python app.py
