from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
db.app = app


@app.route('/')
def hello_world():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
