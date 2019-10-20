import json
# Import the resource/controllers we're testing
from flask_restplus import Api, Resource, fields, marshal
from resources.healthcheck import *
from models.healthcheck import healthcheck
from models.signalfxevent import signalfxevent


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

    # Make a test call to /ec2check
    response = client.post("/ec2check", data=json.dumps(data), headers=headers)

    # Validate the response
    assert response.status_code == 200
    assert response.json == {
        "id": "i-0085a516efcc628d6",
        "description": "Python for Dummies"
    }

def test_translate_to_signalfxevent(client):
    data = {
        'id': 'i-0085a516efcc628d6',
        'description': 'Python for Dummies'
    }

    eventObject = marshal(data, healthcheck)
    ec2checks = EC2Checks()
    customsignalevent = ec2checks.translate_to_signalfxevent(eventObject)
    assert customsignalevent['eventType'] == data['id']