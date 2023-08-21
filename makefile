.PHONY: format style tests typecheck

format:
	black --line-length 79 .

style:
	flake8

tests:
	pytest --capture=sys .

typecheck:
	mypy .
