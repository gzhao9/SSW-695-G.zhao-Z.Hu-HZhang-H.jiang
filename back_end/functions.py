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
# with open('apikey.txt', mode='r') as api:
with open('back_end/apikey.txt', mode='r') as api:
    API_KEY = api.read()


# -----------------------table name----------------------------
tablelogin = 'login'

tableuserInfo = 'userInfo_logs'

tablefoodInfo = 'foodinfo'

tablesportInfo = 'basicsportinfo'

tablemealRecord = 'mealRecord'

tablesportRecord = 'sportRecord'



#  -------------------Login function---------------------------
def verify_login(userId,password):
    userInfo = {
    'userId': userId,
    'userPassword': password,
    }
    return flask_db_operate.findIfInTableTwoEle(tablelogin, 'userId', userInfo['userId'], 'userPassword', userInfo['userPassword'])


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

def get_infoId(userId):
    data = flask_db_operate.findEleInTable('infoId', tableuserInfo, 'userId', userId)
    return data


def get_infoIdandfrom():
    colName1 = 'foodId'
    colName2 = 'comefrom'
    data = flask_db_operate.showTwoCol(tablefoodInfo, colName1, colName2)
    list1 = list()
    list2 = list()
    for i in data:
        list1.append(i[0])
        list2.append(i[1])
    res = {
        colName1 : list1,
        colName2 : list2,
    }
    return res


def get_fooodIdandName():
    colName1 = 'foodId'
    colName2 = 'foodName'
    res = flask_db_operate.showTwoCol(tablefoodInfo, colName2, colName1)
    return res
    


def get_user_info(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tableuserInfo, 'userId', userId, 'infoDate', date)

def get_user_logs(userId):
    return flask_db_operate.findInTable(tableuserInfo, 'userId', userId)

def get_food_info(comefrom,foodId):
    try:
        foodId=int(foodId)
    except:
        pass
    if comefrom == 'webapi':
        return json.loads(flask_db_operate.findInTable(tablefoodInfo, 'foodId', foodId))[0]
    else:
        return json.loads(flask_db_operate.findInTableWithTwoLimit(tablefoodInfo, 'comefrom', comefrom, 'foodId', foodId))[0]

def get_exercise_info(sportId):
    return flask_db_operate.findInTable(tablesportInfo, 'sportId', sportId)


def get_deit_logs(userId,date):
    data=json.loads(flask_db_operate.findInTableWithTwoLimit(tablemealRecord, 'userId', userId, 'mealDate', date))
    result=list()
    for i in data:
        if i=={"isNone":True}:
            return i
        foodinfo=get_food_info('webapi',i['foodId'])
        tem={
		'food_name': foodinfo['foodName'],
		'type': i['mealType'],
		'weight': i['unit'],
		'carbohydrate': int(foodinfo['carbohydrate']*i['unit']/100),
		'protein': int(foodinfo['protein']*i['unit']/100),
		'fat': int(foodinfo['fat']*i['unit']/100),
		'calorie_cost': int(foodinfo['energy']*i['unit']/100),
		'mealRecordID': i['mealRecordId']
        }
        result.append(tem)
    return result


def get_exercise_logs(userId,date):
    result = json.loads(flask_db_operate.findInTableWithTwoLimit(tablesportRecord, 'userId', userId, 'sportDate', date))
    for res in result:
        if(res == {'isNone':True}):
            return res
        else:
            res['exercise_name'] = res.pop('exerciseName')
            res['minute'] = res.pop('durition')
    return result


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
        mealdata['foodInfo']['energy']=int(mealdata['foodInfo']['energy']*100/mealdata['unit'])
        mealdata['foodInfo']['carbohydrate']=int(mealdata['foodInfo']['carbohydrate']*100/mealdata['unit'])
        mealdata['foodInfo']['fat']=int(mealdata['foodInfo']['fat']*100/mealdata['unit'])
        mealdata['foodInfo']['protein']=int(mealdata['foodInfo']['protein']*100/mealdata['unit'])
        mealdata['foodId']=update_food_info(userId,mealdata['foodInfo'])


    
    #because when manuallyInput by user, the food info not in database, so it dose not have foodID. update_food_info(userId,info) will return the new foodID store in database.
    del mealdata['foodInfo']
    del mealdata['manuallyInput']
    mealdata['userId']=userId
    mealdata['mealDate']=mealdata.pop("Date")
    return flask_db_operate.insertintoTable(tablemealRecord, mealdata)

def aaa(userId,info):
    info['comefrom'] = userId
    flask_db_operate.insertintoTable(tablefoodInfo, info)
    foodId = flask_db_operate.findId()[0]
    return foodId

def update_exercise_info(userId,info):
    info['userId'] = userId
    info['durition'] = info.pop('minute')
    info['sportDate'] = datetime.now()
    return flask_db_operate.insertintoTable(tablesportRecord, info)


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

# ------------------------get food nutrient-------------------------------
def call_food_API(foodName):
    foodInfoList = get_food_nutrient.call_API(foodName, API_KEY)
    foodFormatList = format_food_detail(foodInfoList,foodName)
    if len(foodFormatList)>0:
        return foodFormatList[0]
    else:
        return None


def food_search(userId,keyword):
    namelist=get_fooodIdandName()
    namelist.reverse()
    result=list()
    for info in namelist:
        if keyword.lower() in info[0].lower() or info[0].lower().startswith(keyword.lower()):
            foodinfo=get_food_info("webapi",info[1])
            if foodinfo['comefrom']==userId or foodinfo['comefrom']=='webapi':
                result.append(foodinfo)
    if len(result)>0:
        return result

    else:
        apifind=call_food_API(keyword)
        if apifind is not None:
            newID=update_food_info("webapi",apifind)
            return [apifind]
        else:
            return [{"isNone":True}]
        

# ------------------------format food info with detail----------------------
def format_food_detail(foodInfoList,foodName):
    fooddatalist = list()
    for i in range(len(foodInfoList['foods'])):
        # fdcId = foodInfoList['foods'][i]['fdcId']
        foodCategory = foodInfoList['foods'][i]['foodCategory']
        foodDetailInfo = foodInfoList['foods'][i]['foodNutrients']
        # foodName = foodInfoList['foods'][i]['lowercaseDescription']
        fooddata = get_food_nutrient.format_food(foodName, foodCategory, foodDetailInfo)
        fooddatalist.append(fooddata)
        # break after 10 result
        if i <= 10:
            break
    
    return fooddatalist

# --------------------------recommandation----------------------------------
def give_recommandation(userId, remaincalorie):
    allergyres = flask_db_operate.findEleInTable('allergySource', tableuserInfo, 'userId', userId)
    allergy = allergyres[len(allergyres) - 1][0]
    if(allergy != '' and allergy != '[]'):
        res = flask_db_operate.recommandinTable(tablefoodInfo, 'energy', remaincalorie, 'foodType', allergy)
    else:
        res = flask_db_operate.recommandinTable(tablefoodInfo, 'energy', remaincalorie, 'foodType', None)
    return res