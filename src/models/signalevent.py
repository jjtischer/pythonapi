from flask_restplus import fields
from server.instance import server

signalCategories =["USER_DEFINED", "ALERT", "AUDIT", "JOB", "COLLECTED", "SERVICE_DISCOVERY", "EXCEPTION"]

signalevent = server.api.model('signalEvent', {
    'category': fields.String(description='category', enum=signalCategories, required=True),
    'eventType': fields.String(description='name of custom event', required=True, min_length=1, max_length=256),
    'dimensions': fields.String(description='dimensions' ),  #need custom validator to avoid _|sf_ max_length 128
    'properties': fields.String(description='properties', required=True, min_length=1, max_length=256),#need custom validator to avoid _aws
    'timestamp': fields.DateTime(description='timestamp', required=True, dt_format='iso8601'),
})



