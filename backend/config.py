from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config:
  """Contains the configuration for the application."""

  HOST = os.getenv('HOST', 'localhost')
  PORT = os.getenv('PORT', '5000')
  DEBUG = os.getenv('DEBUG', True)
  SQLALCHEMY_DATABASE_URI = os.environ.get(
      'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
