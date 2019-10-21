from server.instance import server
import sys, os

# Need to import all resources
from resources.healthcheck import *
#gunicorn needs 'application'
application = server.app

if __name__ == '__main__':
    server.run()