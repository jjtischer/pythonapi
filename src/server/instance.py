from flask import Flask
from flask_restplus import Api, Resource, fields
from environments.instance import env_config

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Monitor Service',
            description='Utilities for operations',
            doc = env_config["swagger-url"]
        )

    def run(self):
        self.app.run(
                debug = env_config["debug"],
                port = env_config["port"]
            )

server = Server()