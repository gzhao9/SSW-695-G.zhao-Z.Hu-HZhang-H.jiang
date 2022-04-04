from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv

from datetime import datetime

import get_food_nutrient

import flask_db_operate

with open('back_end\\apikey.txt', mode='r') as api:
    API_KEY = api.read()

todaytime = '2022-4-1'


app = Flask(__name__)

@app.route('/input_food',methods=['GET','POST'])
def input_food():
    reader=list()
    with open('back_end\\USER_INFO\\USER_FOOD_LOGS.CSV', mode='r') as inp:
        readers = csv.reader(inp) 
        reader=[row for row in readers]


    meal_id=food_id=str(len(reader))
    user_name='GW'
    date='2022-03-24'
    food_name=request.form.get('food_name')
    Type=request.form.get('Type')
    weight=request.form.get('weight')
    calorie_rate=request.form.get('calorie_rate')
    carbohydrate=request.form.get('carbohydrate')
    protein=request.form.get('protein')
    fat=request.form.get('fat')
    try:
        calorie_cost=float(calorie_rate)*float(weight)/100
        calorie_cost=str(calorie_cost)
        reader.append([meal_id,food_id,food_name,user_name,date,Type,weight,calorie_rate,carbohydrate,protein,fat,calorie_cost])
        
        with open('back_end\\USER_INFO\\USER_FOOD_LOGS.CSV', 'w') as f:
            s=''
            for key in reader:
                s+=(",".join(key)+'\n')
            f.write(s)
        return redirect('/today/'+ "GW")
    except:
        calorie_cost=0
    return render_template('input_food.html')


@app.route('/yoursituation/<username>', methods =['GET','POST'])
def getinfo(username):
    userId = username
    userName = request.form.get('Name')
    gender = request.form.get('gender')
    height = request.form.get('height')
    weight = request.form.get('weight')
    age = request.form.get('age')
    fatRate = request.form.get('fatRate')
    BMR = request.form.get('BMR')
    infoDate = datetime.now()
    submit = request.form.get('Submit')
    userInfoDict = {
        'userId':userId,
        'userName':userName,
        'gender':gender,
        'height':height,
        'weight':weight,
        'age':age,
        'fatRate':fatRate,
        'BMR':BMR,
        'infoDate':infoDate
    }
    if submit == 'Submit':
        canRecord = flask_db_operate.insertUserInfo(userInfoDict)
        if canRecord:
            return redirect('/home/'+username)
    return render_template('user_info.html')



@app.route('/register',methods=['GET','POST'])
def register():
    
    login=request.form.get('login')
    if login=="login":
         return redirect('/login')
    username=request.form.get('username')
    password=request.form.get('password')
    register=request.form.get('Register')

    userInfo = {
        'userId': username,
        'userPassword': password,
    }
    if(register == 'Register'):
        canreg = flask_db_operate.insertLogin(userInfo)
        if canreg:
            return redirect('/yoursituation/' + username)
    return render_template('register.html',result=False)

@app.route('/')
def inddex():
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    Login = request.form.get('Login')
    Register=request.form.get('Register')
    
    userInfo = {
        'userId': username,
        'userPassword': password,
    }
    cannotlogin = flask_db_operate.findIfInTable('login', 'userId', userInfo['userId'])

    if Login == 'Login':
        if(cannotlogin):
            return redirect('/home/'+username)
    if Register=="Register":
        return redirect('/register')
    return render_template('login.html',result=False)
    

@app.route('/home/<username>',methods=['GET','POST'])
def homepage(username):
    username = username
    userinfo = request.form.get('Check')
    today = request.form.get('today')
    if userinfo == 'Check':
        return redirect('/user_info/'+ username)
    search = request.form.get('Search')
    if search == 'Search':
        return redirect('/searchFood')
    
    if today == 'today':
        return redirect('/today/'+username)
    
    userinfo = flask_db_operate.findInTable('userInfo_logs', 'userId', username)
    # if len(userinfo) == 1:
    userinfores = userinfo[0]
    print(userinfores)
    total = 2300
    
    mealres = flask_db_operate.findInTable('mealRecord', 'mealDate', todaytime)
    totalenergy = 0.0
    for i in mealres:
        canfind = flask_db_operate.findIfInTable('foodInfo', 'foodName', i[4])
        if canfind:
            foodenergy = flask_db_operate.findInTable('foodInfo', 'foodName', i[4])
            totalenergy += foodenergy
        else:
            ans = get_food_nutrient.call_API(i[4], API_KEY)
            foodenergy = ans['foods'][0]['foodNutrients'][3]['value']
            totalenergy += foodenergy
    
    remaind = total - totalenergy

    if remaind>=0:
        advice="You can still enjoy foods today"
    else:
        advice="You ate too much today, need to do exercise."
    return render_template('homepage.html', total = total, remaind = remaind, advice = advice)

@app.route('/today/<username>',methods=['GET','POST'])
def userfoodInfo(username):
    userId = username
    mealDate = request.form.get('mealDate')
    # mealDate = datetime.now()
    mealType = request.form.get('mealType')
    foodName = request.form.get('foodName')
    res_data = flask_db_operate.findInTable('mealRecord', 'mealDate', todaytime)

    mealData = {
        'userId':userId,
        'mealDate':mealDate,
        'mealType':mealType,
        'foodName':foodName,
    }
    
    Inputinfo = request.form.get('Inputinfo')
    if Inputinfo == 'Inputinfo':
        caninput = flask_db_operate.insertMealRecord(mealData)
        if caninput:
            return redirect('/today/' + userId)
    
    ReturnHome = request.form.get('Home')
    if ReturnHome == 'Home':
        return redirect('/home/' + userId)

    return render_template('today.html', rows = res_data)

@app.route('/user_info/<username>',methods=['GET','POST'])
def userInfo(username):
    with open('back_end\\USER_INFO\\USER_BASE_INFO.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = [rows for rows in reader if rows[2]==username or rows[0]=='info_id']
    result=f"<h2>{username}'s info</h2><table><tbody>"
    for row in user_info:
        result+="<tr>"
        for c in row:
            result+=f"<td>{c}</td>"
        result+="</tr>"
    result+="</tbody></table>"
    return render_template('user_info.html',title=f"{username}'s Info logs",rows=user_info)  

@app.route('/searchFood',methods=['GET','POST'])
def searchFood():
    Input= request.form.get('Input')
    foodName = request.form.get('foodname')
    search = request.form.get('Search')
    if Input == 'Input':
        return redirect('/input_food')
    if search == 'Search':
        return redirect('/foodNutrient/' + foodName)
    return render_template('search_food.html')


@app.route('/foodNutrient/<foodname>')
def foodNutrient(foodname):
    foodName = foodname
    # API_KEY = 'JkdjMHjQobEeEAVSkii5eg1n5NtTKH0AAL0FgXBb'
    ans = get_food_nutrient.call_API(foodName, API_KEY)
    fdcId = ans['foods'][0]['fdcId']
    foodCategory = ans['foods'][0]['foodCategory']
    # foodWeight = response['foods'][0]['packageWeight']
    protein = ans['foods'][0]['foodNutrients'][0]['value']
    fat = ans['foods'][0]['foodNutrients'][1]['value']
    carbohydrate = ans['foods'][0]['foodNutrients'][2]['value']
    energy = ans['foods'][0]['foodNutrients'][3]['value']
    sugre = ans['foods'][0]['foodNutrients'][4]['value']
    vitamin_A = ans['foods'][0]['foodNutrients'][9]['value']
    vitamin_C = ans['foods'][0]['foodNutrients'][10]['value']
    data = {
        'foodId': fdcId,
        'foodName': foodName,
        'foodType': foodCategory,
        'protein': protein,
        'fat':fat,
        'carbohydrate':carbohydrate,
        'energy':energy,
        'sugar':sugre,
        'va':vitamin_A,
        'vc':vitamin_C,
    }
    # return data.json()
    insert = flask_db_operate.insertFood(data)
    if insert:
        print("insert successful")
    else:
        print("insert fail")
    return make_response(data)


if __name__ == '__main__':
    app.run()