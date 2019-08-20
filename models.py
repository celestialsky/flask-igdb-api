from peewee import * # import everything from peewe
from flask_login import UserMixin # special mini class, that we can
# inherit from that gives us special properties to help create sessions
import datetime # python module to help deal with dates

# mongoose.connect('mongodbString')
DATABASE = SqliteDatabase('vid_games.sqlite')
# sqlite is just a file on our computer
# this is good for expermination and getting things up and
# running,
# once you have your models perfect, as good as they will be,
# then you would add postgres or mysql (production dbs)

# How to set up the Model
class User(UserMixin, Model):
    username = CharField() # can pass it unique=True
    email = CharField()
    password = CharField()
    image = CharField()

    class Meta:
        # when the class object creates an object
        # we can give it instructions
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True) # safe = true,
    # says look at the tables if they're already creatd don't do naything
    print("TABLES CREATED")
    DATABASE.close()
