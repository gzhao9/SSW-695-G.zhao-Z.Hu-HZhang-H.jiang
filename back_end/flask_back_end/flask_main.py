from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import get_food_nutrient
import csv
#import pandas as pd

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    user_info = {}

    with open('back_end\\flask_back_end\\USER_INFO\\LOGIN.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}

    try:
        result=(user_info[username]!=password)
        if result:
            return redirect(url_for('helloword'))
            
    except:        
        result=True
    return render_template('login.html',result=result)

@app.route('/FoodPage',methods=['GET','POST'])
def helloword():
    return "<h1>food page</h1>"

if __name__ == '__main__':
    app.run()