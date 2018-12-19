class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '2333@66666'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
