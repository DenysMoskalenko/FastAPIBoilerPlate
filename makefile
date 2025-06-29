lint:
	ruff format
	ruff check --fix

lint-no-format:
	ruff check

test:
	pytest

test-coverage:
	pytest --cov=app --cov-report=term-missing --cov-report=html --cov-fail-under=90

run:
	uvicorn app.main:app --reload --port=8000
