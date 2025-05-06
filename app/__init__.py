import os
from flask import Flask, current_app, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .config import Config

db = SQLAlchemy()

from . import models

app = Flask(__name__, static_folder='../dist/assets')
CORS(app)
app.config.from_object(Config)


db.init_app(app)
    
from .api import api_bp
from .client import client_bp

app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

with app.app_context():
    if not os.path.exists('db.sqlite'):
        db.create_all()

