import datetime
import requests
import json
from flask import Flask
from flask_restplus import Api, Resource, fields, marshal

from server.instance import server
from models.healthcheck import healthcheck
from models.signalevent import signalevent
from environments.instance import env_config
from environments.instance import env

#needed for flask
app, api = server.app, server.api

@api.route('/ec2check')
class EC2Checks(Resource):

    @api.expect(healthcheck, validate=True)
    @api.marshal_with(healthcheck)
    def post(self):
        signal_event = self.translate_to_signalevent(api.payload)
        return api.payload, self.send_event(signal_event)

    def translate_to_signalevent(self, healthcheck):
        signaleventdata = {
            'category': "USER_DEFINED",
            'eventType': healthcheck['id'],
            'dimensions': {
                "environment": env,
                "service": "ec2"
            },
            'properties': '',
            'timestamp': datetime.datetime.now()
        }
        eventObject = marshal(signaleventdata, signalevent)
        return eventObject

    def send_event(self, data):
        api_token = env_config["signal_api_key"]
        api_url_base = env_config["signal_api_base_url"]
        headers = {'Content-Type': 'application/json',
                   'X-SF-TOKEN': '{0}'.format(api_token)}

        api_url = '{0}'.format(api_url_base)

        try:
            response = requests.post(api_url, headers = headers,  data = json.dumps(data))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e.response.text)

        return response.status_code

