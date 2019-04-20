class Config:
    '''
    General configuration parent class
    '''
    PITCH_API_BASE_URL = 'https://api.thepitchdb.org/3/pitch/{}?api_key={}'

class ProdConfig(Config):

class DevConfig(Config):

    DEBUG = True
