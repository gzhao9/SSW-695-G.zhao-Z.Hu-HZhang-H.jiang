from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
from functions import *
from datetime import datetime


app = Flask(__name__)

# -------------------Login and Register page---------------------------
@app.route('/verifyLogin', methods = ['GET','POST'])
def verifyLogin():
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_login(data['userId'],data['password']),
    }
    return result

# Register page
@app.route('/verifyRegister', methods = ['GET','POST'])
def verifyRegister():
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_register(data['email'],data['password']),
    }
    return result


#--------------------user info --------------------------

# view and Update userInfo page
@app.route('/updateUserInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):
    data = json.loads(request.get_data())
    data['date']=datetime.strptime(data['date'], '%Y-%m-%d')
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
    return result

#Get a list of all the history information records for a certain user
@app.route('/getUserInfo_logs/<userId>', methods = ['GET','POST'])
def getUserInfo_logs(userId):    
    result=get_user_logs(userId)
    return result

@app.route('/delete_user_info', methods = ['GET','POST'])
def delete_user_info():    
    data = json.loads(request.get_data())
    isSuccess=delete_user_info(data['mealId'])
    result= {
        "isSuccess":isSuccess,
    }
    return result


#---------------------------diet info----------------------------------------

@app.route('/updateDietInfo/<userId>', methods = ['GET','POST'])
def updateDietInfo(userId):
    data = json.loads(request.get_data())
    isSuccess=update_food_info(userId,data)
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
    data = json.loads(request.get_data())
    result=get_deit_logs(userId,datetime.strptime(data['date'], '%Y-%m-%d'))
    return result

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
    data = json.loads(request.get_data())
    result=get_exercise_info(userId,datetime.strptime(data['date'], '%Y-%m-%d'))
    return result
@app.route('/delete_Exercise', methods = ['GET','POST'])
def delete_Exercise(userId):
    data = json.loads(request.get_data())
    isSuccess=delete_sport_info(data['sportRecordId'])
    result= {
        "isSuccess":isSuccess,
    }
    return result

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)