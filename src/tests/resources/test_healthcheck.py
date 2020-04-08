import json
import pytest
import requests, unittest
import requests_mock
# Import the resource/controllers we're testing
from flask_restplus import Api, Resource, fields, marshal
from resources.healthcheck import *
from models.healthcheck import healthcheck
from models.signalevent import signalevent
from environments.instance import env_config


# client is a fixture, injected by the `pytest-flask` plugin
def test_post_healthcheck(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'id': 'i-0085a516efcc628d6',
        'description': 'Python for Dummies'
    }
    #response = client.post("/ec2check", data=json.dumps(data), headers=headers)

    ec2checks = EC2Checks()
    with requests_mock.Mocker() as m:
        m.post(env_config["signal_api_base_url"], text='mock', status_code=200)
        assert ec2checks.send_event(data) == 200



def test_translate_to_signalevent(client):
    data = {
        'id': 'i-0085a516efcc628d6',
        'description': 'Python for Dummies'
    }

    eventObject = marshal(data, healthcheck)
    ec2checks = EC2Checks()
    customsignalevent = ec2checks.translate_to_signalevent(eventObject)
    assert customsignalevent['eventType'] == data['id']