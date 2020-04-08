#Overview
This is a simple Python utilities API.

#Responsibilities
- Accept a POST request from our internal service and translate this into a new signal event

#Requirements 
- Correctly accept a POST request from our internal health service
- Correctly POST a new event to signal (https://developers.signal.com/ingest_data_reference.html)
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

#running with gunicorn
gunicorn -b 0.0.0.0:8080 --chdir src main

#docker
./d.sh run
```

#Docker Usage
```
./d.sh build|run|stop|cli|logs|test|docs
```
 
- Your project will need to provide a build tool (Bash, Makefile, etc) to do the following:
- docker: build the container 
- docker-run: build the container and run the service
- docker-shell: run a shell inside a pre-made container
- docker-test: run python tests on an already running container

 
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
pipenv install pytest-mock
pipenv install requests_mock
pipenv install gunicorn

#Resources
https://nikgrozev.com/2018/10/12/python-api-with-flask-and-flask-restplus/
https://flask-restplus.readthedocs.io/en/stable/example.html
https://gunicorn.org/
https://www.toptal.com/flask/flask-production-recipes
https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3
https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a
https://flask-restplus.readthedocs.io/en/stable/swagger.html#documenting-with-the-api-response-decorator
https://medium.com/@hmajid2301/testing-with-pytest-mock-and-pytest-flask-13cd968e1f24

