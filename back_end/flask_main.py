from math import remainder
from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv
#import pandas as pd

import get_food_nutrient

import flask_db_operate

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

@app.route('/register',methods=['GET','POST'])
def register():
    
    login=request.form.get('login')
    if login=="login":
         return redirect('/login')
    username=request.form.get('username')
    password=request.form.get('password')
    user_info = {}

    with open('back_end\\USER_INFO\\LOGIN.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}
    result=None

    if username is not None:
        if username in user_info.keys():
            result=True
        else:
            user_info[username]=password                    
            with open('back_end\\USER_INFO\\LOGIN.CSV', 'w') as f:
                for key in user_info.keys():
                    f.write("%s,%s\n" % (key, user_info[key]))

            if username in user_info.keys():
                return redirect('/login')

    return render_template('register.html',result=result)

@app.route('/')
def inddex():
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')


    user_info = {}
    with open('back_end\\USER_INFO\\LOGIN.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}
    
    
    
    Register=request.form.get('Register')
    if Register=="Register":
         return redirect('/register')
    
    
    result=None
    try:
        result=(user_info[username]!=password)
        if not result:
            return redirect('/home/'+username)
    except:        
        result=False
    return render_template('login.html',result=result)

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
    
    reader=list()
    with open('back_end\\USER_INFO\\USER_FOOD_LOGS.CSV', mode='r') as inp:
        readers = csv.reader(inp)
        reader=[row for row in readers]
    total=[float(a[-1]) for a in reader if a[3]=="GW" and a[4]=='2022-03-24' ]
    
    remaind=2400
    total=int(sum(total))
    remaind=remaind-total
    if remaind>=0:
        advice="You can still enjoy foods today"
    else:
        advice="You ate too much today, need to do exercise."
    return render_template('homepage.html',remaind=remaind,total=total,advice=advice)

@app.route('/today/<username>',methods=['GET','POST'])
def userfoodInfo(username):
    with open('back_end\\USER_INFO\\USER_FOOD_LOGS.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = [rows for rows in reader if (rows[3]==username and rows[4]=='2022-03-24') or rows[0]=='meal_id']
    #print(user_info)
    #return "<p>Hello, World!</p>"
    result=f"<h2>{username}'s info</h2><table><tbody>"
    for row in user_info:
        result+="<tr>"
        for c in row:
            result+=f"<td>{c}</td>"
        result+="</tr>"
    result+="</tbody></table>"
    #return result
    return render_template('user_info.html',title=f"{username} Foods logs",rows=user_info)

@app.route('/user_info/<username>',methods=['GET','POST'])
def userInfo(username):
    with open('back_end\\USER_INFO\\USER_BASE_INFO.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = [rows for rows in reader if rows[2]==username or rows[0]=='info_id']
    #print(user_info)
    #return "<p>Hello, World!</p>"
    result=f"<h2>{username}'s info</h2><table><tbody>"
    for row in user_info:
        result+="<tr>"
        for c in row:
            result+=f"<td>{c}</td>"
        result+="</tr>"
    result+="</tbody></table>"
    #return result
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
    #  with open('back_end\\apikey.txt', mode='r') as api:
    #    API_KEY = api.read()
    API_KEY = 'JkdjMHjQobEeEAVSkii5eg1n5NtTKH0AAL0FgXBb'
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