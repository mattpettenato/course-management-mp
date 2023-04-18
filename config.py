import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Set the secret key to a random string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    
    # Set the database URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://thomasp:Pett29@localhost/golfcourse'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
