import models
import requests
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict # from peewee

game = Blueprint('games', 'game', url_prefix='/game')

@game.route('/', methods=["POST", "GET"])
def index():
    r = requests.post('https://api-v3.igdb.com/games/', data=
    "fields name, popularity, cover; sort popularity desc; limit 50;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    return jsonify(games=r)
