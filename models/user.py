from db import db

class User_model(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30))
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    def user_save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def user_delete_account(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return User_model.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, userid):
        return User_model.query.filter_by(id=userid).first()
