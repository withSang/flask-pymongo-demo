"""
Demo Image Generator Blueprint
"""
import datetime
import random
from flask import Blueprint
from flask_restx import Api, Resource, reqparse, fields

from database import mongo

blueprint = Blueprint('image', __name__)
api = Api(
    blueprint,
    version='1.0',
    title='Image API',
    description='A simple Image Generator API',
    doc="/docs"
)

# defines the parameters required by the API
# and response types
prompt_parser = reqparse.RequestParser()
prompt_parser.add_argument('prompt', type=str, required=True, help='Prompt for the image')
prompt_parser.add_argument('user_id', type=str, required=True, help='User ID')
response_model = api.model('Image', {
    'url': fields.String,
})

@api.route("/generate")
class Image(Resource):
    """
    Demo Image Generator API
    Returns random image URL
    """
    @api.expect(prompt_parser)
    @api.response(200, 'Successed', response_model)
    def get(self):
        """
        Returns random image URL
        """
        args = prompt_parser.parse_args()
        user_id = args['user_id']
        prompt = args['prompt']

        # generate a random image
        image_idx = random.randint(1, 400)
        sample_url = f"https://picsum.photos/id/{image_idx}/536/354"

        # create log
        mongo.db.image_log.insert_one({
            "user_id": user_id,
            "prompt": prompt,
            "url": sample_url,
            "timestamp": datetime.datetime.utcnow(),
        })

        return {"url": sample_url}
