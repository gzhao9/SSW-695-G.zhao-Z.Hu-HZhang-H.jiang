from flask import Flask,make_response,json,render_template,request,redirect,url_for
from wtforms import StringField,PasswordField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo

import json
import csv

app = Flask(__name__)

app.config['SECRET_KEY']= 'ADJLAJDLA'

class Register(FlaskForm):
    username = StringField(label='username:', validators=[DataRequired('Username can not empty!')])
    password = PasswordField(label='password:', validators=[DataRequired('Password can not empty!')])
    password2 = PasswordField(label='password again:', validators=[DataRequired('Password can not empty!'),EqualTo('password')])
    submit = SubmitField(label='submit')

@app.route('/register',methods=['GET','POST'])
def register():
    form = Register()
    if request.method == 'GET':
        return render_template('register.html',form=form)
    if request.method == 'POST':
        return render_template('register.html',form=form)



if __name__ == '__main__':
    app.run()