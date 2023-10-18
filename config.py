import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY =os.urandom(24).hex()
UPLOAD_FOLDER ='static/uploads'
SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URI')