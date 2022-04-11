from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime
from datetime import date


import get_food_nutrient

import flask_db_operate

# -----------------------table name----------------------------
tablelogin = 'login'

tableuserInfo = 'userInfo_logs'

tablefoodInfo = 'foodInfo'

tablesportInfo = 'basicsportinfo'

tablemealRecord = 'mealRecord'

tablesportRecord = 'sportRecord'



#  -------------------Login function---------------------------
def verify_login(userId,password):
    userInfo = {
    'userId': userId,
    'userPassword': password,
    }
    return flask_db_operate.findIfInTable(tablelogin, 'userId', userInfo['userId'])


#  -------------------Register function---------------------------
def verify_register(userId,password):
    userInfo = {
        'userId': userId,
        'userPassword': password,
    }
    canreg = flask_db_operate.insertintoTable(tablelogin,userInfo)
    return canreg

# -------------------obtain info function---------------------------
def get_BMR(userId):
    BMR = flask_db_operate.findInTable(tableuserInfo, 'userId', userId)
    return BMR

def get_user_info(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tableuserInfo, 'userId', userId, 'infoDate', date)

def get_user_logs(userId):
    return flask_db_operate.findInTable(tableuserInfo, 'userId', userId)

def get_food_info(userId,foodId):
    return flask_db_operate.findInTableWithTwoLimit(tablefoodInfo, 'userId', userId, 'foodId', foodId)

def get_exercise_info(userId,sportId):
    return flask_db_operate.findInTableWithTwoLimit(tablesportInfo, 'userId', userId, 'sportId', sportId)

def get_deit_logs(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tablemealRecord, 'userId', userId, 'mealDate', date)

def get_exercise_logs(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tablesportRecord, 'userId', userId, 'sportDate', date)


#--------------------------update information-----------------------------
def update_user_info(userId,info):
    age=19
    info['userId']=userId
    info['BMR']=cal_BMR(info['gender'],info['weight'],info['height'],age)
    info['fatRate'] # calculation
    return flask_db_operate.insertintoTable(tableuserInfo, info)

def update_food_info(userId,info):
    return flask_db_operate.updateinTable(tablemealRecord, info, 'userId', userId)

def update_exercise_info(userId,info):
    return flask_db_operate.updateinTable(tablesportRecord, info, 'userId', userId)


# --------------------------delete information----------------------------
def delete_user_info(infoId):
    return flask_db_operate.deleteinTable(tableuserInfo, 'infoId', infoId)

def delete_meal_info(mealId):
    return flask_db_operate.deleteinTable(tablemealRecord, 'mealRecordId',mealId)

def delete_sport_info(sportRecordId):
    return flask_db_operate.deleteinTable(tablesportRecord, 'sportRecordId',sportRecordId)
# -------------------------calculation function---------------------------
def cal_BMR(gender,weight,height,age):
    if gender.lower().startswith('m'):
        return 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        return 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
