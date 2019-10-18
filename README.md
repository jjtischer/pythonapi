#Overview
This is a simple Python utilities API.

#Responsibilities
- Accept a POST request from our internal service and translate this into a new SignalFX event

#Requirements 
- Correctly accept a POST request from our internal health service
- Correctly POST a new event to SignalFX (https://developers.signalfx.com/ingest_data_reference.html)
- Run as a Docker container
- is Unit Tested
- has a build tool
- has documentation

#Environments
*MONITORAPP_ENV to set environment*
see src/environments/instance.py for options

#How to run
```
pipenv shell
PYTHON_ENV=prod python src/main.py
```

#Docker Usage

- Your project will need to provide a build tool (Bash, Makefile, etc) to do the following:
- docker: build the container
- docker-run: build the container and run the service
- docker-shell: build the container and run a shell inside it
- docker-test: build the container and run any test suite you have

#Sample Data
The expected POST request from our internal service
```
Sample POST Request
{
    "id": "i-0085a516efcc628d6",
    "description": "This server is unhealthy"
}
```

  
#Python requirements 
brew install pipenv
pipenv install flask
pipenv shell
pipenv install flask-restplus
pipenv install pytest
pipenv install pytest-flask

