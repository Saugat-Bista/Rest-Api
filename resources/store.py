from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
          
    def get(self, name):
        store= StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "'{}' already exists.".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured inserting the store."}, 500
        return store.json(), 201
    
    def delete(self, name):
        store= StoreModel.find_by_name(name)
        if store == None:
            return {'message': 'Store not found'}, 404
        else:
            store.delete_from_db()
            return {'message': 'Store deleted'}

class Stores(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
