from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config:
    ''' Configuration '''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/MealPlan'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)
db = SQLAlchemy(app)


# create login table
class foodInfo(db.Model):
    __tablename__ = 'foodInfo'
    foodId = db.Column(db.Integer, primary_key = True)
    foodName = db.Column(db.String(128))
    foodType = db.Column(db.String(128))
    protein = db.Column(db.Float(6,2))
    fat = db.Column(db.Float(6,2))
    carbohydrate = db.Column(db.Float(6,2))
    energy = db.Column(db.Float(6,2))
    sugar = db.Column(db.Float(6,2))
    va = db.Column(db.Float(6,2))
    vc = db.Column(db.Float(6,2))


# create meal record table
class mealRecord(db.Model):
    __tablename__ = 'mealRecord'
    mealRecordId = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.String(128), unique = True)
    mealDate = db.Column(db.Date)
    mealType = db.Column(db.CHAR(2))
    foodId = db.Column(db.Integer, db.ForeignKey('foodInfo.foodId'))

if __name__ == '__main__':
    #clear
    db.drop_all()
    #create
    db.create_all()

    # #insert
    # food1 = foodInfo(foodId = 1, foodName = 'Chadder cheese', foodTpye = 'cheese', protein = 25.0, fat = 32.1, carbohydrate = 3.57, energy = 393,sugar = 0, va = 1070, vc = 0)

    # db.session.add(food1)