from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
from rsa import verify
from functions import *


app = Flask(__name__)


@app.route('/verifyLogin', methods = ['GET','POST'])
def login():
    """
data={
password: "aa"
remember: true
username: "aa
}
    """
    data = json.loads(request.get_data())   
    result= {
        "isSuccess":verify_login(data['username'],data['password']),
    }
    return result


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


@app.route('/updateUserInfo/<username>', methods = ['GET','POST'])
def updateUserInfo(username):
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


@app.route('/today_food_record/<username>', methods = ['GET','POST'])
def updateUserInfo(username):

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
