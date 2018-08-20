import os
from dotenv import load_dotenv
load_dotenv(verbose=True)


class Config:
  SECRET_KEY = os.getenv('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = 'false'

  MAIL_SERVER = 'in-v3.mailjet.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.getenv('EMAIL_USER')
  MAIL_PASSWORD = os.getenv('EMAIL_PASS')
  MAIL_DEFAULT_SENDER = os.getenv('EMAIL_SENDER')
