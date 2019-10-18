# Import the resource/controllers we're testing
from resources.healthcheck import *

# client is a fixture, injected by the `pytest-flask` plugin
def test_get_healthcheck(client):
    # Make a tes call to /ec2check/1
    response = client.get("/ec2check/i-0085a516efcc628d6")

    # Validate the response
    assert response.status_code == 200
    assert response.json == {
        "id": "1",
        "description": "Python for Dummies"
    }