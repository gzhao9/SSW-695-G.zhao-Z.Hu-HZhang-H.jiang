from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
from functions import *
from datetime import datetime
from  planB import *

app = Flask(__name__)
#------------for test----------
@app.route('/test/<username>', methods = ['GET','POST'])
def test(username):
    data=get_user_logs(username)
    return json.dumps(data)

# -------------------Login and Register page---------------------------
@app.route('/verifyLogin', methods = ['GET','POST'])
def verifyLogin():
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_login(data['userID'],data['password']),
    }
    return result

# Register page
@app.route('/verifyRegister', methods = ['GET','POST'])
def verifyRegister():
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_register(data['userID'],data['password']),
    }
    return result


#--------------------user info --------------------------

# view and Update userInfo page
@app.route('/updateUserInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):
    data = json.loads(request.get_data())
    #data['date']=datetime.strptime(data['date'], '%Y-%m-%d')
    isSuccess=update_user_info(userId,data)
    result= {
        "isSuccess":isSuccess,
    }
    return result

#Get the basic information of a user on a certain day
@app.route('/getUserInfo/<userId>', methods = ['GET','POST'])
def getUserInfo(userId):    
    data = json.loads(request.get_data())
    result=get_user_info(userId,datetime.strptime(data['date'], '%Y-%m-%d'))
    return json.dumps(result)

#Get a list of all the history information records for a certain user
@app.route('/getUserInfo_logs/<userId>', methods = ['GET','POST'])
def getUserInfo_logs(userId):    
    result=get_user_logs(userId)
    return result

#Get a list of all last information records for a certain user
@app.route('/get_last_UserInfo/<userId>', methods = ['GET','POST'])
def get_last_UserInfo(userId):    
    result= json.loads(get_user_logs(userId))
    return result[-1]

@app.route('/delete_user_info', methods = ['GET','POST'])
def delete_user_infos():    
    data = json.loads(request.get_data())
    isSuccess=delete_user_info(data['infoId'])
    result= {
        "isSuccess":isSuccess,
    }
    return result


#---------------------------diet info----------------------------------------

@app.route('/updateDietInfo/<userId>', methods = ['GET','POST'])
def updateDietInfo(userId):
    data = json.loads(request.get_data())
    isSuccess=update_meal_info(userId,data)
    result= {
        "isSuccess":isSuccess,
    }
    return result

@app.route('/getDietInfo/<userId>', methods = ['GET','POST'])
def getDietInfo(userId):    
    data = json.loads(request.get_data())
    result=get_food_info(userId,data['foodID'])
    return result

@app.route('/getDietLogs/<userId>', methods = ['GET','POST'])
def getDietLogs(userId):    
    #data = json.loads(request.get_data())
    #result=get_deit_logs(userId,datetime.strptime(data['date'], '%Y-%m-%d'))
    exmaple=[
        {
		'food_name': "cookie",
		'type': "B",
		'weight': 254,
		'carbohydrate': 25,
		'protein': 45,
		'fat': 15,
		'calorie_cost': 635,
		'mealRecordID': 18
        },
        {
		'food_name': "apple",
		'type': "LA",
		'weight': 122,
		'carbohydrate': 11,
		'protein': 22,
		'fat': 33,
		'calorie_cost': 444,
		'mealRecordID': 19
        },
        {
		'food_name': "pizza",
		'type': "D",
		'weight': 1,
		'carbohydrate': 2,
		'protein': 3,
		'fat': 4,
		'calorie_cost': 666,
		'mealRecordID': 20
        }
    ]
    exmaple=json.dumps(exmaple)
    return exmaple

@app.route('/delete_food', methods = ['GET','POST'])
def delete_food():
    data = json.loads(request.get_data())
    isSuccess=delete_meal_info(data['mealId'])
    result= {
        "isSuccess":isSuccess,
    }
    return result
#---------------------------Exercise info----------------------------------------

@app.route('/updateExerciseInfo/<userId>', methods = ['GET','POST'])
def updateExerciseInfo(userId):
    data = json.loads(request.get_data())
    isSuccess=update_exercise_info(userId,data)
    result= {
        "isSuccess":isSuccess,
    }
    return result

@app.route('/getExerciseInfo/<userId>', methods = ['GET','POST'])
def getExerciseInfo(userId):    
    data = json.loads(request.get_data())
    result=get_exercise_info(userId,data['foodID'])
    return result

@app.route('/getExerciseLogs/<userId>', methods = ['GET','POST'])
def getExerciseLogs(userId):    
    #data = json.loads(request.get_data())
    #result=get_exercise_logs(userId,datetime.strptime(data['date'], '%Y-%m-%d'))
    exmaple=[
        { 'exercise_name': "Run", 'minute': 30, 'calorie': 100
        },
        { 'exercise_name': "Walk", 'minute': 30, 'calorie': 100
        },
        { 'exercise_name': "Baseball", 'minute': 30, 'calorie': 100
        },
        { 'exercise_name': "Basketball", 'minute': 30, 'calorie': 100
        }
    ]
    return json.dumps(exmaple)

@app.route('/delete_Exercise', methods = ['GET','POST'])
def delete_Exercise(userId):
    data = json.loads(request.get_data())
    isSuccess=delete_sport_info(data['sportRecordId'])
    result= {
        "isSuccess":isSuccess,
    }
    return result

@app.route('/serach_food_result/<userId>', methods = ['GET','POST'])
def seraching_food_result(userId):
    #data = json.loads(request.get_data())
    result=[
        {
            'foodId':11,
            'food_name': "pizza",
            'carbohydrate': 2,
            'protein': 3,
            'fat': 4,
            'energy':40
            },
            
        {
            'foodId':12,
            'food_name': "zas",
            'carbohydrate': 2,
            'protein': 3,
            'fat': 4,
            'energy':54
            },
            
        {
            'foodId':13,
            'food_name': "aaaa",
            'carbohydrate': 2,
            'protein': 3,
            'fat': 4,
            'energy':125
            },            
    ]
    return json.dumps(result)

if __name__ == "__main__":
    app.run()