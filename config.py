from app import app

SECRET_KEY = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golfcourse.db'
