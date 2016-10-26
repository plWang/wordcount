import os
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = False
TESTING = False
CRSF_ENABLED = True
SECRET_KEY = "wangpl9203"
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:wangpl9203@localhost/wangpenglin"

class Config(object):
    DEBUG = False
    TESTING = False
    CRSF_ENABLED = True
    SECRET_KEY = "wangpl9203"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:wangpl9203@localhost/wangpenglin"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



