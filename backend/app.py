from flask import Flask
from config import Config

Config.init()
app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
