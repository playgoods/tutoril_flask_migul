import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SENDER= 'Flasky Admin <mohmed_e@hotmail.com>'
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_ADMIN ="mohmed_e@hotmail.com"
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = "cakephp.php@gmail.com"
	MAIL_PASSWORD = "zfvluxtohgbhloew"
	FLASK_POSTS_PER_PAGE = 10
	FLASKY_POSTS_PER_PAGE = 5
	FLASKY_FOLLOWERS_PER_PAGE = 5
	FLASKY_COMMENTS_PER_PAGE= 5
	
	
	@staticmethod
	def init_app(app):
		pass
		

class DevelopmentConfig(Config):
	DEBUG = True
	
	SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL')or\
		'sqlite:///'+os.path.join(basedir,'data_dev.sqlite')
		
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL')or\
		'sqlite:///'+os.path.join(basedir,'data_test.sqlite')
		
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')
		
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
	
    'default': DevelopmentConfig
}