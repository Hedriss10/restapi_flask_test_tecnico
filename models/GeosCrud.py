from geoalchemy2 import Geometry
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class ItemModel(db.Model):
    """
    Neste models de ORM com SQLALchemy mais o geoalchemy iremos criar o database com a seguite regrea
    
    Definimos o nome da tabela com `itens` 
    
    id definimos uma coluna chamada `id` que armazena até 30 cacarteres e contém uma chave primária 
    
    name definimos uma coluna chamada `name` que armazena até 30 caracteres e não pode ser um campo nulo
    
    desception definimos uma coluna chamada `descreption` que armazena um texto e não pode ser nulo
    
    geomtry definimos uma coluna chamada `geometry` que armazena dados geonetricos do tipo (point)  \
        com o sistema de referencia espacial srid(4326) e também não permite valores nulos
    
    """
    __tablename__ = "itens"
    
    id = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    descreption = db.Column(db.Text, nullable=False)
    geometry = db.Column(Geometry('POINT', srid=4326), nullable=False)
    
    # inicializador da class item 
    def __init__(self, id, name, descreption, geometry):
        self.id =  id 
        self.name = name
        self.descreption = descreption 
        self.geometry = geometry
        
    
    # funçao para retornar um json 
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "descreption": self.descreption,
            "geometry": str(self.geometry)  # Convertendo a geometria para WKT
        }
        
    # funcão para buscar por id o item     
    @classmethod
    def find_id(cls, id):
        item = cls.query.filter_by(id=id).first()
        return item
    
    
    # função para salvar o item o db de dados
    def save_id(self):
        db.session.add(self)
        db.session.commit()
        
    # função para atualizar o item 
    def update_id(self, id, name, descreption, geometry):
        self.id = id 
        self.name =  name 
        self.descreption = descreption
        self.geometry = geometry
        
    # função para apagar no db de dados 
    def delete_id(self):
        db.session.delete(self)
        db.session.commit()
        
    
    
    # Função para fazer a busca item que esta em um raio especifico 
    @classmethod
    def find_nearest_satellite(cls, latitude, longitude, radius):
        """
        Primeiro vamos declarar uma variavel e point e  
        ST_MakePoint do PostgreSQL com as coordenadas de latitude e longitude fornecidas. 
        A função ST_SetSRID é usada para definir explicitamente o SRID (Sistema de Referência Espacial) como 4326 garantindo que corresponda ao SRID da geometria na coluna
        cls.geometry que está presento no banco de dados 

        --- 
        Segundo a vamos declarar uma variavel result é usada para aplicar a condição ST_DWithin 
        que verifica se a geometria da tabela (cls.geometry) está dentro do raio especificado do ponto criado anteriormente. 
        Em seguida, order_by é usado para ordenar os resultados pela distância entre a geometria e o ponto. 
        Finalmente, all() é chamado para executar a consulta e obter uma lista de resultados.
    
        """    
    
        
        point = func.ST_SetSRID(func.ST_MakePoint(longitude, latitude), 4326)

        result = cls.query.filter(
            func.ST_DWithin(cls.geometry, point, radius)
        ).order_by(
            func.ST_Distance(cls.geometry, point)
        ).all()  # Usando o metedo all() para obter uma lista simples 

        return result
    
    
class UsersModel(db.Model):
    """
        Nessa class vamos criar o cadastro do Users 
        Definimos uma coluna chamada `user_id` do tipo interger e sendo de chave primaria 
        Definimos uma coluna chamada `login` que contém um campo de até 40 caracteres 
        Definimos uma coluna chamada `senha` que contém um campo de até 40 caracteres 

    """ 
    
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40))
    senha = db.Column(db.String(40))
    
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
            }

    # função para buscar o id         
    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None


    # função para buscar o usuario pelo o login 
    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None


    # função para salvar o usuario
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    # função para deletar  o usuario
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
