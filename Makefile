# ==================================================================================== # 
# HELPERS
# ==================================================================================== #
## help : print message for each command usage
.PHONY: help
help:
	@echo "Usage:"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

# ==================================================================================== # 
# BUILD
# ==================================================================================== #
## build_image: runs docker build to create docker image
.PHONY: build_image
build_image:
	docker build .

## docker_build: builds and runs a docker container
.PHONY: docker_build
docker_build:
	docker-compose build

## docker_up: runs the container with logs
.PHONY: docker_up
docker_up:
	docker-compose up

## docker_down: stops all containers runing
.PHONY: docker_down
docker_down:
	docker-compose down

## start_front: starts the frontend app by vue
.PHONY: start_front
start_front:
	@echo "Starting front end"
	@cd front && npm run serve

## start_back: starts the backend with docker in detach
.PHONY: start_back
start_back:
	@echo "Starting back end"
	docker-compose up -d

## back_front: starts both the frontend and backend
.PHONY: back_front
back_front: start_back start_front

# ==================================================================================== # 
# DEVELOPMENT
# ==================================================================================== #

## migrate_up: runs makemigrations and migrate for new apps with models
.PHONY: migrate_up
migrate_up:
	docker-compose run --rm api sh -c "python manage.py makemigrations && python manage.py migrate"

# ==================================================================================== # 
# QUALITY CONTROL
# ==================================================================================== #
## tests: runs all pytests
.PHONY: tests
tests:
	docker-compose run --rm api sh -c "pytest"

## test_v: runs all pytests verbosely and show print commands
.PHONY: test_v
test_v:
	docker-compose run --rm api sh -c "pytest -s -v"

## lint: checks linting based on flake8
.PHONY: lint
lint:
	docker-compose run --rm api sh -c "flake8"
