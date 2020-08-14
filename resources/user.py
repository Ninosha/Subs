from flask_restful import Resource, reqparse
from models.user import User_model
from security import authenticate, identity
from flask_jwt import JWT
import sqlite3


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="შეიყვანეთ სახელი")


    def post(self, name):
        data = User.parser.parse_args()
        if User_model.find_by_username(name):
            return {'message': f'username {name} უკვე არსებობს'}, 404
        try:
            account = User_model(name, data['password'])
            account.user_save_to_db()
        except Exception as k:
            return {"message": k}


    def delete(self, name):
        item = User_model.find_by_name(name)
        if item:
            item.user_delete_account()
            return {'message': 'მონაცემი წაშლილია'}
        else:
            return {'message': 'მონაცემი ბაზაში ვერ მოიძებნა'}
