from dotenv import load_dotenv
import os


class Config:
  """Contains the configuration for the application."""

  @classmethod
  def init(cls):
    load_dotenv()

    cls.HOST = os.getenv('HOST', 'localhost')
    cls.PORT = os.getenv('PORT', '5000')
    cls.DEBUG = os.getenv('DEBUG', True)
