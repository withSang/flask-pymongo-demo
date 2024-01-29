"""
Demo Image Generator Blueprint
"""
import datetime
import io
import os
import random
import uuid

from flask import Blueprint, url_for
from flask_restx import Api, Resource, reqparse, fields
import grpc
from PIL import Image as PILImage
from werkzeug.exceptions import InternalServerError

from app.protos import generate_image_pb2, generate_image_pb2_grpc
from database import mongo
from config import Config

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
        request_id = f"{int(datetime.datetime.utcnow().timestamp())}_{str(uuid.uuid4())}"
        user_id = args['user_id']
        prompt = args['prompt']

        # connect to gRPC server
        channel = grpc.insecure_channel(Config.GRPC_SERVER_URI, options=[
            ('grpc.max_send_message_length', 10 * 1024 * 1024), # 10MB
            ('grpc.max_receive_message_length', 10 * 1024 * 1024) # 10MB
        ])
        stub = generate_image_pb2_grpc.ImageGenerationStub(channel)

        # call gRPC server
        generate_image_response = stub.GenerateImage(
            generate_image_pb2.GenerateImageRequest(
                prompt=prompt,
            )
        )

        if generate_image_response.success:
            # image = PILImage.frombytes(
            #     "RGB",
            #     (generate_image_response.image.width, generate_image_response.image.height),
            #     generate_image_response.image.data,
            #     "raw"
            # )
            image = PILImage.open(
                io.BytesIO(generate_image_response.image.data)
            )

            # save image to static folder
            image_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../static/user-generated", f"{request_id}.png")
            )
            with open(image_path, "wb") as f:
                image.save(f, "PNG")

            image_url = f'{Config.HOST}{url_for("static", filename=f"user-generated/{request_id}.png")}'

            # create log
            mongo.db.image_log.insert_one({
                "request_id": request_id,
                "user_id": user_id,
                "prompt": prompt,
                "url": image_url,
                "timestamp": datetime.datetime.utcnow(),
            })

            return {"url": image_url}
        else:
            e = InternalServerError("The image generation service is currently down. Please try again later.")
            raise e
