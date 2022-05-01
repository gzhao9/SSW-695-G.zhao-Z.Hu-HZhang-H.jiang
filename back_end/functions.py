from math import remainder
from tkinter import N
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime
from datetime import date


import get_food_nutrient

import flask_db_operate
from fitness_tools.meals.meal_maker import MakeMeal
# -------------------------API config----------------------
# with open('apikey.txt', mode='r') as api:
with open('back_end/apikey.txt', mode='r') as api:
    API_KEY = api.read()


# -----------------------table name----------------------------
tablelogin = 'login'

tableuserInfo = 'userinfo_logs'

tablefoodInfo = 'foodinfo'

tablesportInfo = 'basicsportinfo'

tablemealRecord = 'mealrecord'

tablesportRecord = 'sportrecord'



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

def get_user_info1(userId,date):
    #return flask_db_operate.findInTableWithTwoLimit(tableuserInfo, 'userId', userId, 'infoDate', date)
    user_logs=get_user_logs(userId)
    user_logs=json.loads(user_logs)
    for i in range(1,len(user_logs)):
        if date >= user_logs[i-1]['infoDate'] and date < user_logs[i]['infoDate']:
            result= user_logs[i-1]
    if date >= user_logs[-1]['infoDate']:
        result=user_logs[-1]
    #result['infoDate']=datetime.strptime( result['infoDate'], '%Y-%m-%d')
    return result

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
    info['BMR']=cal_info(info['weight'],info['height'],info['fatRate'],info['gender'],info['mealPlan'])['max_calories']
    info['fatRate'] # calculation

    info['infoDate']=info.pop('date')
    info['userName']=info.pop('fullName')

    info['isVegan']=1 if info['isVegan'] is True else 0

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
    if mealdata['manuallyInput'] is True:
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

def cal_info(weight,height,fat,gender,goal):
    #calculate the BMI and Fat
    h=height/100
    over_fat=None
    over_bmi=None
    if gender.lower().startswith('m'):        
        over_fat=True if fat>25 else over_fat        
        over_fat=False if fat<15 else over_fat
    else:    
        over_fat=True if fat>30 else over_fat        
        over_fat=False if fat<20 else over_fat
    bmi=weight/(h*h)
    over_bmi =True if bmi>18.5 else over_bmi   
    over_bmi =False if bmi<=18.5 else over_bmi   
    
    #get the body type of user
    bodr_type='mesomorph' 
    if over_bmi is True and over_fat is True:
        bodr_type='endomorph'
    if over_fat is False:
        bodr_type='mesomorph' 
    if over_bmi is False and over_fat is True:
        bodr_type='ectomorph'
    
    if goal=="buildMuscle":
        goal="weight_gain"
    elif goal=='keepHealth':
        goal="maintenance"
    elif goal=="loseWeight":
        goal="weight_loss"
    else:
        goal=None
    
    weight=int(weight*2.2)
    obj = MakeMeal(weight, goal=goal, activity_level='moderate',
               body_type=bodr_type).daily_requirements()
    obj['body_type']=bodr_type
    return obj

# ------------------------get food nutrient-------------------------------
def call_food_API(foodName):
    foodInfoList = get_food_nutrient.call_API(foodName, API_KEY)
    foodFormatList = format_food_detail(foodInfoList,foodName)
    if len(foodFormatList)>0:
        return foodFormatList[0]
    else:
        return None

def food_statistic():
    fooddate = flask_db_operate.showTable(tablefoodInfo)
    return fooddate





def food_search(userId,keyword):
    
    namelist=get_fooodIdandName()
    namelist.reverse()
    result=list()
    for info in namelist:
        if keyword.lower() in info[0].lower() or info[0].lower().startswith(keyword.lower()):
            foodinfo=get_food_info("webapi",info[1])
            if foodinfo['comefrom']==userId or foodinfo['comefrom']=='webapi':
                result.append(foodinfo)
                if len(result)>6:
                    return result
    if len(result)>0:
        return result

    else:
        apifind=call_food_API(keyword)
        if apifind is not None:
            newID=update_food_info("webapi",apifind)
            return [get_food_info("webapi",newID)]
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


def give_advise(userId,date):
    """

    the advise includr 3 parts:body advise, meal advise, food recommandation
    At the homepage, the body advise and meal advise will shown as text in
    At the mealrecords page, the food recommandation will shown as the choice.

    """
    # ------------------advise about body------------------------
    #read the user body info
    info=json.loads(get_user_logs(userId))[-1]
    body_data=cal_info(info['weight'],info['height'],info['fatRate'],info['gender'],info['mealPlan'])
    #get the body type and give the adivse.
    body_advise={
        'endomorph':"Your body is endomorph. You should lower your body fat percentage and maintain muscle. Endomorphs have a medium to large frame and tend to be very shapely.", 
        'ectomorph':"Your body is ectomorph. You have a very perfect body shape, keep it!",
        'mesomorph':"Your body is mesomorph. you have little mass (fat and muscle). You need to gain weight. "
    }

    body_advise=body_advise[body_data['body_type']]
    #===================================================================================

    #===================diet advise===============================================
    #get the food logs set defeaut advise is remaind to eat somethings
    dietres = get_deit_logs(userId,date)
    foodAdvise="No eating foods. Advice will given after eating."
    #if not eat eveythings, recomend the first 3 foods added
    if dietres == {"isNone":True}:
        foor_Rec=food_search(userId,'')[:5]
        return {
            "Advise":{"advice":body_advise+"\n"+foodAdvise},
            "recomandationFoods":foor_Rec
	}

    #calcuate the dara of foods
    carbohydrate = 0
    protein = 0
    fat = 0
    calorie = 0
    for i in dietres:
        carbohydrate += i['carbohydrate']
        protein += i['protein']
        fat += i['fat']
        calorie += i['calorie_cost']
    limitation ={
        'over_carbohydrate':0,
        'over_protein':0,
        'over_fat':0,
        'over_calorie':0,
    }
    # cal weather over eat.
    if carbohydrate>body_data['max_carbs']:
        limitation['over_carbohydrate']=carbohydrate-body_data['max_carbs']
    elif carbohydrate<body_data['min_carbs']:
        limitation['over_carbohydrate']=carbohydrate-body_data['min_carbs']

    if fat>body_data['max_fat']:
        limitation['over_fat']=fat-body_data['max_fat']
    elif fat<body_data['min_fat']:
        limitation['over_fat']=fat-body_data['min_fat']

    if protein>body_data['max_protein']:
        limitation['over_protein']=protein-body_data['max_protein']
    elif protein<body_data['min_protein']:
        limitation['over_protein']=protein-body_data['min_protein']

    if calorie>body_data['max_calories']:
        limitation['over_calorie']=calorie-body_data['max_calories']
    elif calorie<body_data['min_calories']:
        limitation['over_calorie']=calorie-body_data['min_calories']


    # give the advise of differen item of over eat.
    if limitation['over_calorie']>=0:
        foodAdvise="You have enough calorie intake for today."
    else:
        if (limitation['over_carbohydrate']>=0 and limitation['over_fat']>=0 and limitation['over_protein']>=0) or (limitation['over_carbohydrate']<0 and limitation['over_fat']<0 and limitation['over_protein']<0):
            foodAdvise=f"\nYou can eat at whatever you want"
            for k,v in limitation.items():
                if k=='over_calorie':
                    continue
                foodAdvise+=f"\n {k[5:]} \t Remaining:{-1*v} grams"
        else:
            for k,v in limitation.items():
                if v>=0:                    
                    foodAdvise+=f"\nYou are over eat the {k[5:]} by {v} grams, Avoid foods containing {k[5:]}"
                else:
                    if k=='over_calorie':
                        continue
                    foodAdvise+=f"\nYour {k[5:]} intake is not enough, you at least get {-1*v} grams of {k[5:]} from food"
    #======================
    foor_Rec=food_search(userId,'')[:3]
    result={
            "Advise":{"advice":body_advise+"\n"+foodAdvise},
            "recomandationFoods":foor_Rec
	}
    return result
    