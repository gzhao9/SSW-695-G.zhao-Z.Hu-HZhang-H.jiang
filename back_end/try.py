from flask import Flask
app = Flask(__name__)
@app.route('/verifyLogin', methods = ['GET','POST'])
def login():
    # username=request.form.get('username')
    # password=request.form.get('password')
    # Login = request.form.get('Login')
    # Register=request.form.get('Register')
    
    # userInfo = {
    #     'userId': username,
    #     'userPassword': password,
    # }
    # cannotlogin = flask_db_operate.findIfInTable('login', 'userId', userInfo['userId'])

    json = {
        "isSuccess": True,
    }
    # if Login == 'Login':
    #     if(cannotlogin):
    #         return redirect('/home/'+username)
    # if Register=="Register":
    #     return redirect('/register')
    # return render_template('login.html',result=False)
    return json

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
