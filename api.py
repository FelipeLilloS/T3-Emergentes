# Creacion de API REST con Python3, SQLite 3

from flask import Flask, jsonify, request
import game_controller
from db import create_tables

app = Flask(__name__)

@app.route('/games', methods=['GET'])
def get_games():
    games = game_controller.get_games()
    return jsonify(games)


def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=5000, debug=False)