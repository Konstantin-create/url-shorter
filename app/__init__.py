# Configs import
from config import Config

# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask init
app = Flask(__name__)
app.config.from_object(Config)

# DB init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.modules.models import *
from app.routes import *
