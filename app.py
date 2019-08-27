from flask import Flask, g, request, jsonify
from flask_cors import CORS
from flask_login import LoginManager
import models
import requests
from playhouse.shortcuts import model_to_dict
import json
import os


from api.user import user
# from api.games import game

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="", static_folder="static")

app.secret_key = "SDLKGNSDRANDOM STRING"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
CORS(app, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(game, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(user)
# app.register_blueprint(game)

@app.before_request
def before_request():
    """Connect to database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    ''' Close the database connection after each request '''
    g.db.close()
    return response


@app.route('/games', methods=["POST", "GET"])
def index():
    r = requests.post('https://api-v3.igdb.com/games/', data=
    "fields name, popularity, cover, summary, aggregated_rating, release_dates; sort popularity desc; limit 50;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    print (jsonify(r.json()), '<+++ this is games')

    return jsonify(games=r.json())


@app.route('/playstation', methods=["POST", "GET"])
def playstation():
    r = requests.post('https://api-v3.igdb.com/release_dates/', data=
    "fields game; where game.platforms = 48 & date > 1566600380; sort date asc;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    gamelist = []
    print(r.json())
    for game in r.json():
        gamelist.append(str(game["game"]))

    g = requests.post('https://api-v3.igdb.com/games/', data=
    "fields name, cover, summary, aggregated_rating, release_dates.human; where id = (" + ','.join(gamelist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    coverlist = []
    for game in g.json():
        coverlist.append(str(game["id"]))

    p = requests.post('https://api-v3.igdb.com/covers/', data=
    "fields url; where game = (" + ','.join(coverlist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    print(p.json(), "all the covers boiiiiiiiiiiiiiii")
    # print(g.json(), "all the game boiiiiiiii")
    return jsonify(images=p.json(), games=g.json(), date=r.json())


@app.route('/xbox', methods=["POST", "GET"])
def xbox():
    r = requests.post('https://api-v3.igdb.com/release_dates/', data=
    "fields game; where game.platforms = 49 & date > 1566600380; sort date asc;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    gamelist = []
    print(r.json())
    for game in r.json():
        gamelist.append(str(game["game"]))

    g = requests.post('https://api-v3.igdb.com/games/', data=
    "fields name, cover, summary, aggregated_rating, release_dates.human; where id = (" + ','.join(gamelist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    coverlist = []
    for game in g.json():
        coverlist.append(str(game["id"]))

    p = requests.post('https://api-v3.igdb.com/covers/', data=
    "fields url; where game = (" + ','.join(coverlist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    print(p.json(), "all the covers boiiiiiiiiiiiiiii")
    # print(g.json(), "all the game boiiiiiiii")
    return jsonify(images=p.json(), games=g.json())


@app.route('/pc', methods=["POST", "GET"])
def pc():
    r = requests.post('https://api-v3.igdb.com/release_dates/', data=
    "fields game, human; where game.platforms = 6 & date > 1566600380; sort date asc;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    gamelist = []
    print(r.json())
    for game in r.json():
        gamelist.append(str(game["game"]))

    g = requests.post('https://api-v3.igdb.com/games/', data=
    "fields name, cover, summary, aggregated_rating, release_dates.human; where id = (" + ','.join(gamelist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    coverlist = []
    for game in g.json():
        coverlist.append(str(game["id"]))

    p = requests.post('https://api-v3.igdb.com/covers/', data=
    "fields url; where game = (" + ','.join(coverlist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    print(p.json(), "all the covers boiiiiiiiiiiiiiii")
    # print(g.json(), "all the game boiiiiiiii")
    return jsonify(images=p.json(), games=g.json())


@app.route('/nintendo', methods=["POST", "GET"])
def nintendo():
    r = requests.post('https://api-v3.igdb.com/release_dates/', data=
    "fields game, human; where game.platforms = 130 & date > 1566600380; sort date asc;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    gamelist = []
    print(r.json())
    for game in r.json():
        gamelist.append(str(game["game"]))

    g = requests.post('https://api-v3.igdb.com/games/', data=
    "fields name, cover, summary, aggregated_rating, release_dates.human; where id = (" + ','.join(gamelist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    coverlist = []
    for game in g.json():
        coverlist.append(str(game["id"]))

    p = requests.post('https://api-v3.igdb.com/covers/', data=
    "fields url; where game = (" + ','.join(coverlist) + ");",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    return jsonify(images=p.json(), games=g.json())

# @app.route('/search', methods=["POST"])
# def search():
#     query = request.form.to_dict()
#     print(query['data'])
#     query_string = "fields *;search " + "".join(query['data'].split()) + "; limit 50;"
#
#     r = requests.post('https://api-v3.igdb.com/search', data=
#     query_string,
#     headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})
#
#     print(r.json())
#     return jsonify(data=r.json())


if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
