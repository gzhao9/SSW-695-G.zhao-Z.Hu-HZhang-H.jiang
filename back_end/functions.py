from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime

import get_food_nutrient

import flask_db_operate

def verify_login(username,password):
    userInfo = {
    'userId': username,
    'userPassword': password,
    }
    return flask_db_operate.findIfInTable('login', 'userId', userInfo['userId'])

def verify_register(username,password):
    userInfo = {
        'userId': username,
        'userPassword': password,
    }
    canreg = flask_db_operate.insertLogin(userInfo)
    return canreg

def today_food_record(username):
    pass