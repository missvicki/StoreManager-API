install:
	pip install -r requirements.txt

test:
	python3 -m pytest -vv test.py

format:
	black *.py


lint:
	pylint --disable=R,C hello.py

all: install lint test
