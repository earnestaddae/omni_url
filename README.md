# Omni URL 
A simple url shortener with django rest framework api and vue3 as frontend


## Installations
Ensure the following are installed
- [Python v3.10.5]() 
- [Pyenv]()
- [Docker]()
- [nodejs]()
- vue3 with `sudo npm install -g @vue/cli`
- [Postgresql]()
- Ensure you have make install for 
    - Ubuntu - `sudo apt install make`
    - MacOS - `brew install make`
    - Windows - `choco install make`

**NB**: _With the exception of the `npm install` command, all command must run at the root of the `omni_url` directory. Also running the application with docker is highly recommended since most of the make commands assumed docker is installed and running on your machine_

## Cloning Instructions
- Clone the repo into any directory of yours with `git clone git@github.com:earnestaddae/omni_url.git`

## Running Local Instructions
- Create a python virtual environment
- Run `pip install -r requirements.txt`
- Run `createdb omnihrdb` to create database
- Run `python manage.py makemigrations && python manage.py migrate`
- Run `python manage.py runserver`

## Docker Instructions
- Run `make help` to view the make commands
- Change directory into the **front** directory and run `npm install` to get the node_modules for vue
- Run `make build_image` to create a docker image for the api
- Run `make docker_build` to create a container instance of the api

## Linting / Testing Instructions
- Run `make lint` to run flake8
- Run `make tests` to run tests 
- Run `make test_v` to run tests in verbose mode

## Running Instructions 
- Run `make start_back` to start the api 
- Run  `make start_front` to start the frontend
- Run  `make back_front` to start both the back and front ends

## Visiting Instructions
- ### Backend
    - Runs on `http://localhost:8000`
    - Visit `http://localhost:8000/api/docs` to view the endpoints
- ### Frontend 
Runs on `http://localhost:8080`

