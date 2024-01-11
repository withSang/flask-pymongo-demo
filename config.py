import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))  # load environment variables from .env file

class Config:
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/demo'
