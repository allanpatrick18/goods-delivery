# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://test:test@localhost:5432/'
database_name = 'test_db'


class BaseConfig:
    """Base configuration."""
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = os.environ['DB_USER']
    DB_URI = os.environ['DB_URI']
    DB_PASSWORD = os.environ['DB_PASSWORD']


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI'] + database_name
    DB_USER = os.environ['DB_USER']
    DB_URI = os.environ['DB_URI']
    DB_PASSWORD = os.environ['DB_PASSWORD']


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

