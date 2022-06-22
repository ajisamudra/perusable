docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

makemigrations:
	docker-compose exec server python manage.py makemigrations

migrate:
	docker-compose exec server python manage.py migrate

test:
	docker-compose exec server python manage.py test

psql:
	docker-compose exec database psql -U perusable
