"""
Demo Echo Blueprint
"""
from flask import Blueprint
from flask_restx import Api, Resource, fields

blueprint = Blueprint('echo', __name__)
api = Api(
    blueprint,
    version='1.0',
    title='Echo API',
    description='A simple Echo API',
    doc="/docs"
)

echo_model = api.model('Echo', {
    'message': fields.String(required=True, description='Message to echo'),
})

@api.route("/")
class Echo(Resource):
    """
    Demo Echo API
    Echos the request payload
    """
    @api.expect(echo_model)
    def post(self):
        """
        Echo a message
        """
        return api.payload
