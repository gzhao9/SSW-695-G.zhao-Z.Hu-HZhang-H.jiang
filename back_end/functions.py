from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime
from datetime import date


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

def get_food_info(userId,foodID):
    pass

def get_exercise_info(userId,exercise_name):
    pass

def get_user_info(userId,date):
    pass

def get_deit_logs(userId,date):
    pass

def get_exercise_logs(userId,date):
    pass

def get_user_logs(userId):
    pass


def update_user_info(userId,info):
    age=int(info['date'][:4])-int(info['birthday'][:4])
    info['userId']=userId
    info['BMR']=cal_BMR(info['gender'],info['weight'],info['height'],age)
    
    #save info to database @hengyuan

def update_exercise_info(userId,info):
    pass

def update_food_info(userId,info):
    pass

def cal_BMR(gender,weight,height,age):
    if gender.lower().startswith('m'):
        return 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        return 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
