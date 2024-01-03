"""
Script para configurar o sistema de desenvolvimento do Flask, com ele podemos setar no terminal
e escolher se vamos trabalhar com o sistema de desenvolvimento ou test. Ou produção, 
e com isso pode ficar mais fácil o sistema de desenvolvimento
"""
import os

class Config:
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:1234@localhost/apirestflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'secretest'

class ProductionConfig(Config):
    # adcionando a produção de acordo com a necessidade 
    pass

# Mapeando a config das de acordo com as classes 
config_by_name = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig(),
}

# Obtenha o valor da variável de ambiente FLASK_ENV com o padrão 'desenvolvimento'
flask_env = os.getenv('FLASK_ENV', 'development')

# Certifique-se de que flask_env seja uma chave válida em config_by_name
if flask_env not in config_by_name:
    raise ValueError(f"Invalid value for FLASK_ENV: {flask_env}. Must be one of {list(config_by_name.keys())}")

# Obtenha o objeto de configuração correspondente
config = config_by_name[flask_env]
