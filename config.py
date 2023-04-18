# from app import app

# SECRET_KEY = 'your-secret-key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golfcourse.db'


class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///golfcourse.db'

class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/golfcourse'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
