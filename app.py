"""
This module should done:
* GET /homepage
"""

from flask import Flask

app = Flask(__name__)

store_info = [
    {
        "name": 'First Store',
        "items":[
            {
                "name": "First Item",
                "price": 22.22,
            }
        ]
    }
]


@app.route("/homepage", methods=['GET'])
def homepage():
    return {"Message": "Hello web! This is homepage!"}

if __name__ == "__main__":
    app.run(port=8080, debug=True)
