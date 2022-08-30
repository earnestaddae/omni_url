lint:
	docker-compose run --rm api sh -c "flake8"

docker_build:
	docker-compose build

docker_up:
	docker-compose up

docker_down:
	docker-compose down

migrate_up:
	docker-compose run --rm api sh -c "python manage.py makemigrations && python manage.py migrate"

tests:
	docker-compose run --rm api sh -c "pytest"