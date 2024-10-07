import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ["SECRET_KEY"]
ENV = os.environ["ENV"]
DEBUG = bool(ENV == "dev")
LOGIN_TIMESTAMP_FORMAT = os.environ["LOGIN_TIMESTAMP_FORMAT"]

DB_HOST = os.environ.get("DB_HOST", "japanese_recognition-db-1")
DB_NAME = os.environ.get("DB_NAME", "japanese_recog")
DB_USER = os.environ.get("DB_USER", "japanese_recog_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "H1ragana")
APP = os.environ.get("APP", "src.app.main:app")
