from flask_restful import Resource,reqparse
from flask_jwt import jwt_required, JWT
from models.Items import Item_model

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('breed',
                        type=str,
                        required=True,
                        help="gtxovt sheiyvanot nivtierebis tipi")
    @jwt_required()
    def get(self, name):
        item = Item_model.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': f' {name} უკვე არის ბაზაში'}, 404

    def post(self, name):
        if Item_model.find_by_name(name):
            return {'message': f'მონაცემი {name} უკვე არსებობს'}, 404
        try:
            data = Item.parser.parse_args()
        except Exception as t:
            return {"message": t}
        item = Item_model(name, data["breed"])
        item.save_to_db()
        return {'message': f'{name} დაემატა ბაზაში'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = Item_model.find_by_name(name)
        if item:
            item.breed = data['breed']
        else:
            item = Item_model(name, data['breed'])
        item.save_to_db()
        return item.json()

    def delete(self, name):
        item = Item_model.find_by_name(name)
        if item:
            Item_model.delete_from_db(item)
            return {'message': 'მონაცემი წაშლილია'}
        else:
            return { 'message' : 'მონაცემი ბაზაში ვერ მოიძებნა'}


class Items_List(Resource):
    @jwt_required()
    def get(self):
        items = Item_model.query.filter_by().all()
        items_list = []
        for a in items:
            items_list.append(a.json())
        return {"message": items_list}