from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.Items import Item_model



class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('breed',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ ნივთიერების ტიპი")

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ ნივთიერების დასახელება")

    @jwt_required()
    def get(self, name):
        hal = ["LSD", "Ketamine"]
        stim = ["Meth", "Crack", "Cocaine", "Amphetamine"]
        dep = ["Alcohol", "Heroin"]
        item = Item_model.find_by_name(name)
        if name in hal:
            return {'message': f"{name} არის ჰალუცინოგენი. {name}ის როგორც ჰალუცინოგენის მიღება შემდეგ ნივთიერებებთან არის საშიში: {dep}"}
        if name in stim:
            return {'message': f"{name} არის სტიმულატორი. {name}ის როგორც სტიმულატორის მიღება შემდეგ ნივთიერებებთან არის საშიში: {dep}"}
        if name in dep:
            return {'message': f" {name} არის დეპრესანტი. {name}ის როგორც დეპრესანტის მიღება შემდეგ ნივთიერებებთან არის საშიში: {hal} და {stim}"}
        else:
            return {'message': f' {name} ნივთიერება არ არის სიაში'}, 404

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