from contextlib import redirect_stderr
from flask import Flask,make_response,json,render_template,request,redirect,url_for
import json
import get_food_nutrient
import csv
#import pandas as pd

app = Flask(__name__)

@app.route('/login')
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    user_info = {}

    with open('csv_file.csv', mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}
    if user_info[username]==password:
        return redirect(url_for('helloword'))
    else:
        return "<h1>eeeeeeeeeeeee</h1>"
    return render_template('login.html')

@app.route('/FoodPage')
def helloword():
    return "<h1>food page</h1>"

if __name__ == '__main__':
    app.run()