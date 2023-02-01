"""
api.py file!
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

db = [
    {
    "name": "First Stores",
        "item":[
            {
            "name":"First Item",
            "price": 22.22,
            }
        ]
    }
]

@app.route('/stores', methods=['GET'])
def get_stores():
    """
    GET /stores - отдает информацию про все магазиныб какие у нас есть.
    """
    return jsonify({"stores": db}), 200

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name:str):
    """
    GET /store/<string:name> - отдаем информацию про магазин с именем name.
    """
    # Идем по всем магазинам циклом.
    for store in db:
        if store["name"] == name:
            # Возвращаем найденный магазин
            return jsonify(store), 200
    # А если не нашли?
    return jsonify({"Error": "Store with that Name not found!"}), 404

@app.route("/store", methods=["POST"])
def post_store():
    """
    POST /store + data.json - создадим (добавляем в бд новый магазин) с пастым списком товаров. 
    """
    # Получаем все что лежит в теле запроса и перекладываем в dict()
    request_data = request.get_json()
    # request_data = {"name": "NewStore"}
    new_store = {
        'name' : request_data["name"],
        'items': [],
    }
    # Добавляем новый магазин в базу данных
    db.append(new_store)
    # Возвращает в ответ только что созданный новый магазин.
    return jsonify(new_store),201

@app.route('/store/<string:name>', methods=['PUT'])
def put_store(name:str):
    """
    Обновление ассортимента магазина
    """
    # Первым делом проверим, существует ли такой магазин
    for store in db:
        if store["name"] == name:
            request_date = request.get_json()
            store["items"] = request_date["items"]
            return jsonify(store), 202
    return jsonify({"Error" : "Store with that name does not exists"}), 404

@app.route("/store/<string:name>", methods=['DELETE'])
def delete_store(name:str):
    """
    Пытаемся удалить магазин из бд.
    """
    idx = None
    for store in db:
        if store["name"] == name:
            idx = db.index(store)
            break
    if idx:
        db.pop(idx)
        return jsonify({"Message": "Store succesfully deleted"}), 202
    return jsonify({"Error": "Store with that name not found"}),404

if __name__ == "__main__":
    app.run(port=8080, debug=True)