from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

# Initializing flask extensions
def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://emmah:kHAOYAISDEAD2008@localhost/test'
    db = SQLAlchemy(app)

    app.config.from_object(config_options[config_name])

    bootstrap = Bootstrap(app)
