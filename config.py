import os

class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/Pitch'



class Config:
    '''
    General configuration parent class
    '''
    PITCH_API_BASE_URL = 'https://api.thepitchdb.org/3/pitch/{}?api_key={}'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:password@localhost/watchlist_test'    

class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
