from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models  # all the classes and functions are methods on the models object
# name of file is models

from api.user import user


DEBUG = True
PORT = 8000

login_manager = LoginManager()

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__, static_url_path="", static_folder="static")

app.secret_key = "SDLKGNSDRANDOM STRING"
login_manager.init_app(app)

@login_manager.user_loader  # decorator # current_user, or load anything from
# the session
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

CORS(user, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(user)

@app.before_request  # given to us by flask @
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
    # params = {
    #     'api_key': '{2c904db2f8c0bceb80aae9b04132521b}'
    #     }
    # r = requests.get(
    #     'https://api-v3.igdb.com/'
    # )
    return 'hi'  # res.send in express


# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

# peewee is an ORM, mongoose is an ODM
