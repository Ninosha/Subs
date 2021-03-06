from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy

from security import authenticate, identity
from resources.Items import Item, Items_List
from resources.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///datas.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
app.secret_key = 'k'
jwt = JWT(app, authenticate, identity)


@app.route('/')
def home():
    return redirect("https://documenter.getpostman.com/view/11823818/TVK5c1rZ")

api.add_resource(Item, '/items/<string:name>')
api.add_resource(Items_List, '/items')
api.add_resource(User, '/acc')



if __name__ == "__main__":
    from db import db
    db.init_app(app)

app.run(port=5000, debug=True)
