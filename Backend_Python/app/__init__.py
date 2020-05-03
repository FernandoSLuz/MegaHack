from flask import Flask
from .controllers import main, errors
from flask_cors import CORS
# import extensions
# import config

blueprints = (main, errors)

def create_app(debug = False):
   app = Flask(__name__)
   app.secret_key = 'secret'
   CORS(app, resources={r"/*": {"origins": "*"}})
   app.debug = debug
   app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
   # app.config.from_object(config.ConfigObject)
   init_blueprints(app)
   return app

def init_blueprints(app):
   for bp in blueprints:
      app.register_blueprint(bp)