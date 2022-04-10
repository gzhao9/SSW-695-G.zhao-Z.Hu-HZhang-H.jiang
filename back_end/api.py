from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
from functions import *


app = Flask(__name__)

# -------------------Login and Register page---------------------------
@app.route('/verifyLogin', methods = ['GET','POST'])
def login():
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_login(data['userId'],data['password']),
    }
    return result

# Register page
@app.route('/verifyRegister', methods = ['GET','POST'])
def Register():
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_register(data['confirm'],data['password']),
    }
    return result


#--------------------user info --------------------------

# view and Update userInfo page
@app.route('/updateUserInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):
    data = json.loads(request.get_data())
    isSuccess=update_user_info(userId,data)
    result= {
        "isSuccess":isSuccess,
    }
    return result

#Get the basic information of a user on a certain day
@app.route('/getUserInfo/<userId>', methods = ['GET','POST'])
def getUserInfo(userId):    
    data = json.loads(request.get_data())
    result=get_user_info(userId,data['date'])
    return result

#Get a list of all the history information records for a certain user
@app.route('/getUserInfo_logs/<userId>', methods = ['GET','POST'])
def getUserInfo(userId):    
    result=get_user_logs(userId)
    return result


#---------------------------diet info----------------------------------------

@app.route('/updateDietInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):
    data = json.loads(request.get_data())
    isSuccess=update_food_info(userId,data)
    result= {
        "isSuccess":isSuccess,
    }
    return result

@app.route('/getDietInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):    
    data = json.loads(request.get_data())
    result=get_food_info(userId,data['foodID'])
    return result

@app.route('/getDietLogs/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):    
    data = json.loads(request.get_data())
    result=get_deit_logs(userId,data['date'])
    return result

@app.route('/delete_food', methods = ['GET','POST'])
def del_foodInfo():
    data = json.loads(request.get_data())
    pass
#---------------------------Exercise info----------------------------------------

@app.route('/updateExerciseInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):
    data = json.loads(request.get_data())
    isSuccess=update_exercise_info(userId,data)
    result= {
        "isSuccess":isSuccess,
    }
    return result

@app.route('/getExerciseInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):    
    data = json.loads(request.get_data())
    result=get_exercise_info(userId,data['foodID'])
    return result

@app.route('/getExerciseLogs/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):    
    data = json.loads(request.get_data())
    result=get_exercise_info(userId,data['date'])
    return result

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)






























"""

# Home page
@app.route('/home/<userId>',methods=['GET','POST'])
def homePage(userId):
    data = json.loads(request.get_data())
    datetime = data['time']
    #get user nick name
    nickname = flask_db_operate.findEleInTable('userName','userInfo_logs', 'userId', userId)
    #get total calcorie
    BMR = get_BMR(userId,datetime)

    mealres = flask_db_operate.findInTable('mealRecord', 'mealDate', datetime)


    sportres = flask_db_operate.findInTable('sportRecord', 'sportDate', datetime)
    res_BMR = minus_calorie(mealres, BMR)

    result = {
        'nickName':nickname,
        'BMR':res_BMR,
        'mealres':mealres,
        'sportres':sportres,
    }
    return result
"""
