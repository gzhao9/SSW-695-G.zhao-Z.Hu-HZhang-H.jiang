from flask_database import db
from flask_database import foodInfo, mealRecord
from datetime import datetime

import connect_mydb

# db.drop_all()

# db.create_all()
def insertFood(foodDict):
    table = "foodInfo"
    # food1 = foodInfo(foodId = 1, foodName = 'Chadder cheese', foodType = 'cheese', protein = 25.0, fat = 32.1, carbohydrate = 3.57, energy = 393,sugar = 0, va = 1070, vc = 0)
    cols = ','.join("'{}'".format(k) for k in foodDict.keys())
    val_cols = ','.join('%({})s'.format(k) for k in foodDict.keys())
    SQL = "insert into foodInfo(%s) values (%s)"
    RES_SQL = SQL % (cols, val_cols)
    print(RES_SQL)
    mydb = connect_mydb.mydb
    cursor = mydb.cursor()
    # db.session.add(food1)
    # db.session.commit()


# meal1 = mealRecord(mealRecordId = 1, userId = 'gw', mealDate = datetime.utcnow(), mealType = 'L', foodId = food1.foodId)

# db.session.add(meal1)
# db.session.commit()

# foodInfo.query.all()
# mealRecord.query.all()
