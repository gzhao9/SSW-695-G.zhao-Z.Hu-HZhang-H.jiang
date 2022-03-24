from unittest import result
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import csv
#import pandas as pd

app = Flask(__name__)


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

@app.route('/login',methods=['GET','POST'])
def login():
    Register=request.form.get('Register')
    if Register=="Register":
         return redirect('/register')
    username=request.form.get('username')
    password=request.form.get('password')
    user_info = {}

    with open('back_end\\flask_back_end\\USER_INFO\\LOGIN.CSV', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}
    
    try:
        result=(user_info[username]!=password)
        if not result:
            return redirect('/user_info/'+username)
    except:        
        result=False
    return render_template('login.html',result=result)

@app.route('/user_info/<username>',methods=['GET','POST'])
def helloword(username='GW'):
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
    return result
    #return render_template('user_info.html',rows=user_info)

if __name__ == '__main__':
    app.run()