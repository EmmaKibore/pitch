from flask import flask
from .config import DevConfig

# Initializing application
app = Flask(__name__

#setting up configuration
app.config.from_object(DEvConfig)

from app import views
