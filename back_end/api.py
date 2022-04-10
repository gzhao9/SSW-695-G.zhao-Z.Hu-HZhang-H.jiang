from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
from functions import *


app = Flask(__name__)

# Login page
@app.route('/verifyLogin', methods = ['GET','POST'])
def login():
    """
data={
password: "aa"
remember: true
userId: "aa
}
    """
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_login(data['userId'],data['password']),
    }
    return result

# Register page
@app.route('/verifyRegister', methods = ['GET','POST'])
def Register():
    """
data=
{
	confirm: "aaaaaaaa"
    email: "aa@a.com"
    password: "aaaaaaaa"
}
    """
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_register(data['confirm'],data['password']),
    }
    return result

# Home page
@app.route('/home/<userId>',methods=['GET','POST'])
def homePage(userId):
    data = json.loads(request.get_data())
    datetime = data['time']
    """ get user nick name"""
    nickname = flask_db_operate.findEleInTable('userName','userInfo_logs', 'userId', userId)
    """ get total calcorie """
    BMR = get_BMR(userId,datetime)
    """ get meal information in perticular day """
    mealres = flask_db_operate.findInTable('mealRecord', 'mealDate', datetime)

    """ get sport information in perticular day """
    sportres = flask_db_operate.findInTable('sportRecord', 'sportDate', datetime)
    res_BMR = minus_calorie(mealres, BMR)

    result = {
        'nickName':nickname,
        'BMR':res_BMR,
        'mealres':mealres,
        'sportres':sportres,
    }
    return result



# view and Update userInfo page
@app.route('/updateUserInfo/<userId>', methods = ['GET','POST'])
def updateUserInfo(userId):
    """
data=
{
    allergySource: ['fish', 'soy']
    birthday: "2022-04-07"
    fullName: "a"
    height: 1
    isVegan: false
    mealPlan: "keepHealth"
    weight: 1
}
    """
    data = json.loads(request.get_data())


# View meal page

# Insert meal page

# View sport page

# insert sport page

   


@app.route('/today_food_record/<userId>', methods = ['GET','POST'])
def food_record(userId):
    pass

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
