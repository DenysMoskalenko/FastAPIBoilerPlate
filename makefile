lint:
	ruff format
	ruff check --fix

lint-no-format:
	ruff check

up-dependencies:
	docker compose up

test:
	coverage run -m pytest
	coverage report

test-no-coverage:
	pytest

test-html:
	coverage run -m pytest
	coverage html

run_app:
	uvicorn app.main:app --reload --port=8000

migration:
	alembic revision --autogenerate -m "$(MSG)"

migrate:
	alembic upgrade head

upgrade:
	alembic upgrade +1

downgrade:
	alembic downgrade -1
