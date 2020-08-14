from werkzeug.security import safe_str_cmp
from models.user import User_model


def authenticate(username, password):
    user = User_model.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id