import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route('/summation', methods = ['GET', 'POST'])
async def summation(a, b):

    s = add(a, b)

    res = str(s)

    return Response(res)


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=False, port=server_port, host="0.0.0.0")
