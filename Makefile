dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

lint:
	poetry run flake8 task_manager/ --exclude migrations

test:
	poetry run python manage.py test