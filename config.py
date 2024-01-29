import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))  # load environment variables from .env file


class Config:
    """Server configuration related to environment variables."""

    HOST = os.environ.get('HOST') or 'localhost:5024'
    """Server host, prepended to image URL returned to clients"""    
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/demo'
    """MongoDB connection URI"""
    GRPC_SERVER_URI = os.environ.get('GRPC_SERVER_URI') or 'localhost:50051'
    """GRPC server URI"""
