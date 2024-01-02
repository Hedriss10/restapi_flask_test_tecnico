from flask_restful import Resource


class GeosCrud(Resource):
    
    def get(self):
        return {"message" : "Desenvolvimento de dados geospaciais"}