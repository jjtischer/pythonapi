import datetime
from flask import Flask
from flask_restplus import Api, Resource, fields, marshal

from server.instance import server
from models.healthcheck import healthcheck
from models.signalfxevent import signalfxevent

#needed for flask
app, api = server.app, server.api

@api.route('/ec2check')
class EC2Checks(Resource):

    @api.expect(healthcheck, validate=True)
    @api.marshal_with(healthcheck)
    def post(self):
        signalFXEvent = self.translate_to_signalfxevent(api.payload)
        self.sendEvent(signalFXEvent)
        return api.payload

    def translate_to_signalfxevent(self, healthcheck):
        signaleventdata = {
            'category': "USER_DEFINED",
            'eventType': healthcheck['id'],
            'dimensions': '',
            'properties': '',
            'timestamp': datetime.datetime.now()
        }
        eventObject = marshal(signaleventdata, signalfxevent)
        return eventObject

    def sendEvent(self, data):




        return 1
