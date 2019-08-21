from flask import Flask, g, request, jsonify
from flask_cors import CORS
from flask_login import LoginManager
import models
import requests


from api.user import user


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

app.register_blueprint(user)


@app.before_request
def before_request():
    """Connect to database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request  # WE OPEN AND CLOSE TO MANAGE PULL CONNECTIONS SO DONT OL
def after_request(response):
    ''' Close the database connection after each request '''
    g.db.close()
    return response


@app.route('/')
def index():    # can name this method whatever
    r = requests.post('https://api-v3.igdb.com/games/', data= "fields name, popularity; sort popularity desc;",
    headers = {"user-key":"2c904db2f8c0bceb80aae9b04132521b"})

    return jsonify(data=r.json())


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
