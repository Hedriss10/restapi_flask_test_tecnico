"""
Script para configurar o sistema de desenvolvimento do Flask, com ele podemos setar no terminal
e escolher se vamos trabalhar com o sistema de desenvolvimento ou test. Ou produção, 
e com isso pode ficar mais fácil o sistema de desenvolvimento
"""

import os 

class Config(object):
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 5000
    URL_MAIN =  'http://%s:%s/' % (IP_HOST, PORT_HOST)
        
    
app_config = {
    'development': DevelopmentConfig(),
}
app_active = os.getenv('FLASK_ENV')
