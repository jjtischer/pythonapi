#!/bin/bash
#- docker: build the container
#- docker-run: build the container and run the service
#- docker-shell: build the container and run a shell inside it
#- docker-test: build the container and run any test suite you have
SERVICENAME="monitor-service"
function print_usage {
    cat << EOF
Usage: $0 [OPTIONS]
Helper scripts to run $SERVICENAME
Options:
  build|run|stop|cli|logs|test|docs
EOF
}

command="";
TAG=

#need arugments for tags
function docker.build(){
  docker build --tag $SERVICENAME:latest .
}

function docker.run(){
  docker run -d --rm -p 80:8080 --name $SERVICENAME $SERVICENAME:latest
}

function docker.stop(){
  docker container stop $SERVICENAME
}

function docker.cli(){
  docker exec -it $SERVICENAME /bin/bash
}

function docker.logs(){
  docker logs -f $SERVICENAME
}

function docker.test(){
  docker logs -f $SERVICENAME
}


postfix="${@:2:${#1}}";

#docker-compose would be eaiser
case $1 in
  build)
    docker.stop
    docker.build
    ;;
  run)
    docker.stop
    docker.build
    docker.run
    ;;
  stop)
    docker.stop
    ;;
  cli)
    docker.cli $OPTARG
    ;;
  logs)
    docker.logs
    ;;
  docs)
    open http://localhost/api/swagger
    ;;
  test)
    docker.test
    ;;
  *)
    print_usage
    ;;
esac


