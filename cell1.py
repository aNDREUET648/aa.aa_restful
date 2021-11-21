
port = 9999
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')                           # wrappers - a function englobe another function: def route(function)
def hello():
    name = request.args.get("name", "World")
    return "Hello %s!"%name

if __name__ == '__main__':                # double_underscore, curso avanzado
    app.run(port=port, debug=True)
