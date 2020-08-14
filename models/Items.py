from db import db

class Item_model(db.Model):
    __table_name__ = 'subs'

    name = db.Column(db.String(30), primary_key=True )
    breed = db.Column(db.String(30))


    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def json(self):
        return {
            "name": self.name,
            "breed" : self.breed
                }
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

