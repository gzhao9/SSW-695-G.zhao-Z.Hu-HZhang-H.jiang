from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv
#import pandas as pd

import get_food_nutrient

app = Flask(__name__)

@app.route('/input_food',methods=['GET','POST'])
def input_food():
    return render_template('input_food.html')

@app.route('/register',methods=['GET','POST'])
def register():
    
    login=request.form.get('login')
    if login=="login":
         return redirect('/login')
    username=request.form.get('username')
    password=request.form.get('password')
    user_info = {}

    with open('back_end\\flask_back_end\\USER_INFO\\LOGIN.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}
    result=False

    if username is not None:
        if username in user_info.keys():
            result=True
        else:
            user_info[username]=password                    
            with open('back_end\\flask_back_end\\USER_INFO\\LOGIN.CSV', 'w') as f:
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
    with open('back_end\\flask_back_end\\USER_INFO\\LOGIN.CSV', mode='r') as inp:
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
    if userinfo == 'Check':
        return redirect('/user_info/'+ username)
    search = request.form.get('Search')
    if search == 'Search':
        return redirect('/searchFood')
    return render_template('homepage.html')


@app.route('/user_info/<username>',methods=['GET','POST'])
def userInfo(username):
    with open('back_end\\flask_back_end\\USER_INFO\\USER_BASE_INFO.CSV', mode='r') as inp:
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
    return render_template('user_info.html',rows=user_info)

@app.route('/searchFood',methods=['GET','POST'])
def searchFood():
    foodName = request.form.get('foodname')
    search = request.form.get('Search')
    if search == 'Search':
        return redirect('/foodNutrient/' + foodName)
    return render_template('search_food.html')


@app.route('/foodNutrient/<foodname>')
def foodNutrient(foodname):
    foodName = foodname
    with open('back_end\\flask_back_end\\apikey.txt', mode='r') as api:
        API_KEY = api.read()
    ans = get_food_nutrient.call_API(foodName, API_KEY)
    nutrientProtein = ans['foods'][1]['foodNutrients'][0]['value']
    nutrientFat = ans['foods'][1]['foodNutrients'][1]['value']
    nutrientCarbohydrate = ans['foods'][1]['foodNutrients'][2]['value']
    data = {
        'food name:': foodName,
        'nutrient protein:': nutrientProtein,
        'nutrient fat': nutrientFat,
        'nutrient Carbohydrate': nutrientCarbohydrate
    }
    # return data.json()
    return make_response(data)


if __name__ == '__main__':
    app.run()