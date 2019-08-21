# this is like controller from express
# JSONIFY UR BLUEPRINTS

import models
# models, models.Dog, models.User

import os
import sys
import secrets
from PIL import Image


from flask import Blueprint, request, jsonify, url_for, send_file
# Blueprint - record operations to execute (their controllers)

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

# first argument is blueprint name, second is import name, third is what every
# route in the blueprint should start with, much like
# app.use('/api/v1', fruitsCtonroller)

# will have to be registered in the app.py file
user = Blueprint('users', 'user', url_prefix='/user')


@user.route('/register', methods=["POST"])
def register():
    # this is how we grab the image being sent over
    # pay_file = request.files
    # this has the form info in the dict
    # change equest object into a dictionary so we can see inside it
    payload = request.form.to_dict()
    # dict_file = pay_file.to_dict()

    print(payload, "<==== this is the payload")
    # print(dict_file)

    payload['email'].lower()  # make emails lower
    try:
        # check to see if email exists, if it does let user know
        models.User.get(models.User.email == payload['email'])  # query to find
        # user by email
        # if models.User.get exsits then respond to the client
        return jsonify(data={}, status={"code": 401, "message": "a user with the same name or email exists"})
    except models.DoesNotExist:  # boolean on the model
        # otherwise create and regiser the user
        # hash password
        payload['password'] = generate_password_hash(payload['password'])
        # function that will save the image as a static asset in static folder

        # save_picture is hlper function we will create

        # add image property to payload dictionary and save the file_path of img
        # in the db


        # create the row in the sql table
        user = models.User.create(**payload)  # the spread operator in js
        print(type(user))  # >class User user is an instance of class
        # same as aobve this is longhand V
        # user = models.User.create(username=payload['username'], password=payload['password'])

        # start the user session
        login_user(user)  # login_user is from flask_login, set userid in session



        # we cant send back a class we can only send back dicts, lists
        user_dict = model_to_dict(user)
        # make our response object jsonify-able
        # lists, hashs, simple datatype like number bools,
        # NO class or instance of class
        print(user_dict)
        print(type(user_dict))

        # remove the password, client doesn't need to know
        del user_dict['password']

        return jsonify(data=user_dict, status={"code": 201, "message": "Success"})
