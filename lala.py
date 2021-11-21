from flask import Flask
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(user="lala")


if __name__ == "__main__":
    app.run(debug=True)
