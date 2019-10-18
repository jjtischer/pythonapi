from flask import Flask
from flask_restplus import Api, Resource, fields

from server.instance import server
from models.healthcheck import healthcheck

app, api = server.app, server.api

healthcheck_db = [
    {"id": "i-0085a516efccaaaaa", "description": "War and Peace"},
    {"id": "i-0085a516efcc628d6", "description": "Python for Dummies"},
]

@api.route('/ec2check')
class EC2Checks(Resource):

    @api.expect(healthcheck, validate=True)
    @api.marshal_with(healthcheck)
    def post(self):

        return api.payload
