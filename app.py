from flask import Flask
import models  # all the classes and functions are methods on the models object
# name of file is models

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)


# The default URL ends in / ("my-website.com/").
@app.route('/')  # decorator, anything with @, is a function
# before a function
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
