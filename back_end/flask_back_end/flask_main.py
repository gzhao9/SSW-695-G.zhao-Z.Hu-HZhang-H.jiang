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
        if not result:
            return redirect(url_for('helloword'))            
    except:        
        result=False
    return render_template('login.html',result=result)

@app.route('/user_info',methods=['GET','POST'])
def helloword():
    username='GW'
    with open('back_end\\flask_back_end\\USER_INFO\\USER_BASE_INFO.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = [rows for rows in reader if rows[1]==username or rows[0]=='info_id']
    return "<p>Hello, World!</p>"
    render_template('user_info.html',rows=user_info)

if __name__ == '__main__':
    app.run()