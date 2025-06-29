lint:
	ruff format
	ruff check --fix

lint-no-format:
	ruff check

up-dependencies:
	docker compose up

test:
	pytest

test-coverage:
	pytest --cov=app --cov-report=term-missing --cov-report=html --cov-fail-under=90

run:
	uvicorn app.main:app --reload --port=8000

migration:
	alembic revision --autogenerate -m "$(MSG)"

migrate:
	alembic upgrade head

upgrade:
	alembic upgrade +1

downgrade:
	alembic downgrade -1
