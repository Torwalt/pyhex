lint:
	poetry run isort --check .
	poetry run black --check .
	poetry run flake8
	poetry run mypy --install-types --non-interactive -p src -p tests

# open test report in browser, e.g. firefox htmlcov/index.html
tests-cov:
	pytest -svv --cov=src --cov-report=html

db-upgrade:
	poetry run alembic upgrade head

