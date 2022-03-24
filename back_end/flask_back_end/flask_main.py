from flask import Flask,make_response,json,render_template
import json
import get_food_nutrient
#import pandas as pd

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/FoodPage')
def helloword():
    return react("FoodPage.jsx")

if __name__ == '__main__':
    app.run()