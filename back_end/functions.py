from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime
from datetime import date


import get_food_nutrient

import flask_db_operate

# -------------------------API config----------------------
with open('back_end/apikey.txt', mode='r') as api:
    API_KEY = api.read()


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

# -----------------------Insert info into table--------------------
def add_sport():
    sportInfo = {

    }
    flask_db_operate.insertintoTable(tablesportInfo, sportInfo)



# -------------------obtain info function---------------------------
def get_BMR(userId):
    BMR = flask_db_operate.findInTable(tableuserInfo, 'userId', userId)
    return BMR

def get_infoId(userId):
    data = flask_db_operate.findEleInTable('infoId', tableuserInfo, 'userId', userId)
    return data


def get_infoIdandfrom():
    colname1 = 'foodId'
    colname2 = 'comefrom'
    data = flask_db_operate.showTwoCol(tablefoodInfo, colname1, colname2)
    list1 = list()
    list2 = list()
    for i in data:
        list1.append(i[0])
        list2.append(i[1])
    res = {
        colname1 : list1,
        colname2 : list2,
    }
    return res



def get_user_info(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tableuserInfo, 'userId', userId, 'infoDate', date)

def get_user_logs(userId):
    return flask_db_operate.findInTable(tableuserInfo, 'userId', userId)

def get_food_info(comefrom,foodId):
    if comefrom == 'webapi':
        return flask_db_operate.findInTable(tablefoodInfo, 'foodId', foodId)
    else:
        return flask_db_operate.findInTableWithTwoLimit(tablefoodInfo, 'comefrom', comefrom, 'foodId', foodId)

def get_exercise_info(sportId):
    return flask_db_operate.findInTable(tablesportInfo, 'sportId', sportId)

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

    info['infoDate']=info.pop('date')
    info['userName']=info.pop('fullName')

    info['isVegan']=1 if info['isVegan']=='true' else 0

    return flask_db_operate.insertintoTable(tableuserInfo, info)

def update_food_info(userId,foodInfo):
    #store single food info
    #if '@' not in list(userID):#it from api or admin.
    #   set the comefrom as system
    #else: #from user, 
    #   set the comefrom as user
    #return foodID
    if userId == None:
        userId = 'webapi'
    foodInfo['comefrom'] = userId
    flask_db_operate.insertintoTable(tablefoodInfo, foodInfo)
    foodId = flask_db_operate.findId()[0]
    return foodId

def update_meal_info(userId,mealdata):
    if mealdata['manuallyInput']=='true':
        mealdata['foodID']=update_food_info(userId,mealdata['foodInfo'])

    
    #because when manuallyInput by user, the food info not in database, so it dose not have foodID. update_food_info(userId,info) will return the new foodID store in database.
    del mealdata['foodInfo']
    del mealdata['manuallyInput']
    return flask_db_operate.insertintoTable(tablemealRecord, mealdata)

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

# ------------------------format food info with detail----------------------
def format_food_detail(foodInfoList):
    fooddatalist = list()
    for i in range(len(foodInfoList['foods'])):
        # fdcId = foodInfoList['foods'][i]['fdcId']
        foodCategory = foodInfoList['foods'][i]['foodCategory']
        foodDetailInfo = foodInfoList['foods'][i]['foodNutrients']
        fooddata = get_food_nutrient.format_food(foodname, foodCategory, foodDetailInfo)
        fooddatalist.append(fooddata)
        # break after 10 result
        if i >= 10:
            break
    
    return fooddatalist