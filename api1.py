"""
Скелет нашего api
api1.py file!
"""

import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
# Из расширения flask_jwt импортируем:
from flask_jwt import JWT, jwt_required
# Из нашего auth_conf достанем двые функции.
from auth_conf import authenticated, identity

# Сущиность приложения
app = Flask(__name__)
# Секретный ключь нашего приложения (на основе которого будут осуществляться все операции шифрования/дешифрования)
app.secret_key = os.environ.get("SECRET_KEY")

# Сущьность API
api = Api(app)

# сущность БД
db = []

#сущность менеджера токенов.
jwt = JWT(app, authentication_handler=authenticated, identity_handler=identity)

# Ресурс Item /item/<string:name>
class Item(Resource):
    """
    Ресурс, щтвечающий за работу с ОДНОЙ товарной единицей.
    Реализует CRUD.
    """
    parser = reqparse.RequestParser()
    # Нам обязательно нужен price типа float.
    parser.add_argument("price", type=float, required=True, help="Field 'price' required float value!")
    # Нам обязательно нужен amount типа int.
    parser.add_argument("amount", type=int, required=True, help="This field required 'int' value!")
    @jwt_required()
    def get(self, name):
        """
        GET /item/<string:name> - возвращает информацию про товас с именем name.
        """
        item = next(filter(lambda x : x["name"] == name, db ), None)
        if item:
            return {"item": item}, 200
        return {'Error': 'Item with that name not foutd'}, 404

    def post(self, name):
        """
        POST /item/<string:name> - создает товар с имененм name.
        """
        # Проверяем, что бд еще нет товара с таким именем.
        if next(filter(lambda x: x["name"] == name, db), None):
            return {"Error" : f"Item with name {name} already exists!"}, 400

        request_body = Item.parser.parse_args()
        new_item = {"name": name, "price": request_body["price"], "amount": request_body["amount"]}
        db.append(new_item)
        return new_item, 201

    def put(self, name):
        item = next(filter(lambda x : x["name"] == name, db), None)
        if item:
            request_body = Item.parser.parse_args()
            item.update(request_body)
            return item , 202
        return {"Error": f"Item with name {name} not found!"}, 404

    def delete(self, name):
        global db
        start_len = len(db)
        db = list(filter(lambda x : x["name"] != name, db))
        if abs(start_len - len(db)) > 0:
            return {"Message": "Item successfully deleted!"}, 202
        return {"Error": "Item with that name not found"}, 404

# Ресурс Item/ items
class ItemCollection(Resource):
    """
    Ресурс, отвечающий за работу с Множеством товаров.
    """
    def get(self):
        """
        GET /item - возвращает информацию про все товары в магазине.
        """
        return {"database": db}, 200

# Добавим ресурс к API
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemCollection, "/items")

if __name__ == "__main__":
    app.run(port=os.environ.get("PORT"), debug=os.environ.get("DEBUG"))
