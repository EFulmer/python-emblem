format:
	black --line-length 79 .

style:
	flake8

tests:
	pytest

typecheck:
	mypy .
