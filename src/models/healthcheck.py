from flask_restplus import fields
from server.instance import server

healthcheck = server.api.model('HealthCheck', {
    'id': fields.String(description='Id', required=True, min_length=1, max_length=200),
    'description': fields.String(required=False, min_length=1, max_length=200, description='Book title')
})