from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
