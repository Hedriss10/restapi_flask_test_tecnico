from flask_restx import Resource, fields, Api, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from models.GeosCrud import ItemModel, UsersModel

api = Api()

item_model = api.model('Item', {
    'id': fields.String(required=True, description='Identificador único do item'),
    'name': fields.String(required=True, description='Nome do item'),
    'description': fields.String(required=True, description='Descrição do item'),
    'geometry': fields.String(required=True, description='Campo de geometria do tipo Point')
})


geospatial_search_model = api.model('GeospatialSearch', {
    'latitude': fields.Float(required=True, description='Latitude do ponto central'),
    'longitude': fields.Float(required=True, description='Longitude do ponto central'),
    'radius': fields.Float(required=True, description='Raio de busca em unidades específicas')
})


class ItemResource(Resource):
    attrs = reqparse.RequestParser()
    attrs.add_argument("id", type=str, required=True, help="The field 'nome' cannot be left blank.")
    attrs.add_argument("name")
    attrs.add_argument("descreption")
    attrs.add_argument("geometry")
    
    # Implementação para obter um item por ID
    @jwt_required()
    @api.expect(id)  
    def get(self, id):
        search_id = ItemModel.find_id(id=id)
        if search_id:
            # Usando o método json para serializar
            return search_id.json(), 200, {'Content-Type': 'application/json'}
        return {"message": "Id not found."}, 404
    
    # Implementação para criar um novo item
    @jwt_required()
    @api.expect(id)
    def post(self, id):
        if ItemModel.find_id(id=id):
            return {"message": "Item id '{}' already exists".format(id)}
        
        dados = ItemResource.attrs.parse_args()
        novo_item = ItemModel(id=dados['id'], name=dados['name'], descreption=dados['descreption'], geometry=dados['geometry'])

        
        try:
            novo_item.save_id()
        except Exception as e:
            print(e)
            return {"message": "An error occurred trying to create item"}, 500

        return novo_item.json(), 201
    
    # Implementação para atualizar um item por ID
    @jwt_required()
    @api.expect(id)
    def put(self, id):
        dados =  ItemResource.attrs.parse_args()
        search_id = ItemModel(id=dados['id'], name=dados['name'], descreption=dados['descreption'], geometry=dados['geometry']) 
        
        new_search_id = ItemModel.find_id(id=id)
        if new_search_id:
            new_search_id.update_id(**dados)
            new_search_id.save_id()
            return new_search_id.json(), 200 

        search_id.save_id()
        return search_id.json(), 201 


    # Implementação para excluir um item por ID
    @jwt_required()
    @api.expect(id)
    def delete(self, id):
        id =  ItemModel.find_id(id=id)
        if id:
            id.delete_id()
            return {"message" : "Item deleted."}
        return {"message": "Item not found."}, 404

class GeospatialSearch(Resource):
    """
        Classe para fazer a busca de algum item por um ponto determinado 
        Solicitando autenticação do usuário 
    """
    @jwt_required()
    # @api.expect(api.model('GeospatialSearch', {
    #     'latitude': fields.Float(required=True, description='Latitude do ponto central'),
    #     'longitude': fields.Float(required=True, description='Longitude do ponto central'),
    #     'radius': fields.Float(required=True, description='Raio de busca em unidades específicas')
    # }))
    def get(self):
        """
        Metedo de URI get para buscar o item 
        Validando a presença e formato correto dos parâmetros
        Realizando a busca geospacial com GeoAlchemy 
        Retornando via Json 
        """
        args = api.payload
        latitude = args['latitude']
        longitude = args['longitude']
        radius = args['radius']

        if not (latitude and longitude and radius):
            return {"message": "Latitude, longitude, and radius are required parameters."}, 400

        result = ItemModel.find_nearest_satellite(latitude, longitude, radius)

        return {"results": [item.json() for item in result]}, 200

class UserRegistrationResource(Resource):
    """
    Class para registrar o usuário no banco de dados, aonde consiste receber os argumentos como login e senha 
    De acordo com o desenvolvimento o SQLAlchemy já cria o id, fica o nota importante para proseguir com esse modelo de api
    
    """
    attrs = reqparse.RequestParser()
    attrs.add_argument('login', type=str)
    attrs.add_argument('senha', type=str)
    
    # Implementação para registrar um novo usuário
    def post(self):
        dados = UserRegistrationResource.attrs.parse_args()
        if UsersModel.find_by_login(dados['login']):
            return {"message" : "The login '{}' already exists".format(dados['login'])}

        user = UsersModel(**dados)
        user.save_user()
        return {'message': 'User created successfully!'}, 201 # Created
 
class UserAuthenticationResource(Resource):
    """
        Class para criar um token de acesso jwt e repassa para o `acess` para o usuário
        Criando uma métedo de URI post 
    """    
    attrs = reqparse.RequestParser()
    attrs.add_argument('login', type=str)
    attrs.add_argument('senha', type=str)
    
    @classmethod
    def post(cls):
        """
        Declaramos uma variável dados aonde pegamos o attrs que são os atributos da class e passanmos com **kwargs 
        depois fazemos uma busca simples com user ainde comparamos o login no database e o login passando via json
        depois criamos o token com o metedo create_acess_token do jwt e repasamos com o status code 200, e por final
        retornamos uma mensagem de erro se o user estiver passando o login e senha errado
        """    
    
        dados = UserAuthenticationResource.attrs.parse_args()
        user = UsersModel.find_by_login(dados['login'])
        
        if user and user.senha == dados['senha']:
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
            
        return {'message': 'The username or password is incorrect.'}, 401

