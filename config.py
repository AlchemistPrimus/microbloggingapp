import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    MAIL_SERVER=os.environ.get('MAIL_SERVER','smtp.googlemail.com')
    MAIL_PORT=int(os.environ.get('MAIL_PORT','587'))
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS','true').lower() in ['true','on',1]
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    MICROBLOG_MAIL_SUBJECT_PREFIX='[MICROBLOG]'
    MICROBLOG_MAIL_SENDER='Microblog admin <microblog@example.com>'
    MICROBLOG_ADMIN=os.environ.get('MICROBLOG_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MICROBLOG_POSTS_PER_PAGE=25
    SSL_REDIRECT = False
    SQLALCHEMY_RECORD_QUERIES = True
    MICROBLOG_POSTS_PER_PAGE = 10
    MICROBLOG_FOLLOWERS_PER_PAGE = 50
    MICROBLOG_COMMENTS_PER_PAGE = 30
    MICROBLOG_SLOW_DB_QUERY_TIME = 0.5
    UPLOAD_FOLDER='images'
    
    @staticmethod
    def init_app(app):
        """To enable application customize its configurations.
        Takes application instance as its parameter."""
        pass
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'dev-data.sqlite')
    
class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URI') or 'sqlite://'
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data.sqlite')
    
config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}