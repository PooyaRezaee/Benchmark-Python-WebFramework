from flask import Flask
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

@app.route("/")
async def hello_world():
    return "Hello World"

