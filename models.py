from peewee import * # import everything from peewe
from flask_login import UserMixin # special mini class, that we can
# inherit from that gives us special properties to help create sessions
import datetime # python module to help deal with dates


DATABASE = SqliteDatabase('vid_games.sqlite')


class User(UserMixin, Model):
    username = CharField() # can pass it unique=True
    email = CharField()
    password = CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("TABLES CREATED")
    DATABASE.close()
