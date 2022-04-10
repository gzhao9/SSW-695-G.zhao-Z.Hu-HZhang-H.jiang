from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime

import get_food_nutrient

import flask_db_operate

def verify_login(userId,password):
    userInfo = {
    'userId': userId,
    'userPassword': password,
    }
    return flask_db_operate.findIfInTable('login', 'userId', userInfo['userId'])

def verify_register(userId,password):
    userInfo = {
        'userId': userId,
        'userPassword': password,
    }
    canreg = flask_db_operate.insertLogin(userInfo)
    return canreg

def get_BMR(userId):
    BMR = flask_db_operate.findInTable('userInfo_logs', 'userId', userId)
    return BMR



def today_food_record(userId):
    pass