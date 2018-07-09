#init:
#  pip install -r requirements.txt

test:
	python -m pytest -v tests/*

# .PHONY: init test
.PHONY: test
