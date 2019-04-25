import os


class BaseConfig(object):
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    PERMANENT_SESSION_LIFETIME = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(os.getenv("MYSQL"),os.getenv("PYMYSQL"),os.getenv("USERNAME"),os.getenv("PASSWORD"),os.getenv("HOST"),os.getenv("PORT"),os.getenv("SQLNAME"))



class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProduceConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(os.getenv("MYSQL"),os.getenv("PYMYSQL"),os.getenv("USERNAME"),os.getenv("PASSWORD"),os.getenv("HOST"),os.getenv("PORT"),os.getenv("SQLNAME"))



config = {
    "development": DevelopmentConfig,
    "test":TestConfig,
    "produce":ProduceConfig
}