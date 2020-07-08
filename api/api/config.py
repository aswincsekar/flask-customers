import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(os.path.basename(__file__)))


class Config:
    DEBUG = False

    # JWT Config
    JWT_SECRET_KEY = os.urandom(24)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "db.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # PROPAGATE_EXCEPTIONS = True


class ProductionConfig(Config):
    DEBUG = False
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="postgres", pw="postgres", url="postgres:5432",
                                                                   db="postgres")
    SQLALCHEMY_DATABASE_URI = DB_URL
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    default=DevelopmentConfig,
)