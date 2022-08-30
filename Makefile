lint:
	docker-compose run --rm api sh -c "flake8"

docker_build:
	docker-compose build

docker_up:
	docker-compose up

docker_down:
	docker-compose down

tests:
	docker-compose run --rm api sh -c "pytest -v -s"