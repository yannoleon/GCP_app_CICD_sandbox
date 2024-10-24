import os
from flask import Flask, request
from libs.calculus import add

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Test flask app </h1>"

@app.route('/summation', methods = ['POST'])
def summation():
    data = request.json
    a, b = data['a'], data['b']
    s = add(a, b)

    res = str(s)

    return res


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=True, port=server_port, host="0.0.0.0")
