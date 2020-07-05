import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import auth, identity
from resources.user import UserRegister
from resources.item import Item, Items
from datetime import timedelta
from resources.store import Store, Stores

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXPECTATIONS'] = True
app.secret_key= 'abc'
api= Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
jwt= JWT(app, auth, identity)
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)