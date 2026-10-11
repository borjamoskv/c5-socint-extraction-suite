.PHONY: test check install clean

PYTHON ?= python3

test:
	$(PYTHON) tests/test_socint.py

check: test
	$(PYTHON) -m py_compile src/socint/*.py bin/socint tests/*.py

install:
	pip install -e .

clean:
	rm -rf build/ dist/ *.egg-info .eggs src/*.egg-info tests/__pycache__ src/socint/__pycache__
