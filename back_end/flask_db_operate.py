from flask_database_create_table import db
from flask_database_create_table import foodInfo, mealRecord
from datetime import datetime

import connect_mydb
 
mydb = connect_mydb.mydb
mycursor = mydb.cursor()


# insert into foodInfo, if success, return true, else return false
def insertFood(foodDict):
    table = "foodInfo"
    placeholders = ','.join(['%s'] * len(foodDict))
    cols = ','.join(foodDict.keys())
    if findIfInTable(table, 'foodId', foodDict['foodId']):
        SQL = "insert into %s (%s) values (%s);"
        RES_SQL = SQL % ("foodinfo", cols, placeholders)
        # print('RES_SQL:'+RES_SQL)
        mycursor.execute(RES_SQL, list(foodDict.values()))
        mydb.commit()
        return True
    else:
        return False


# find in table where id = colName, if exist, return false, else return true
def findIfInTable(tableName,colName, colValues):
    SQL = "select * from %s where %s = %s"
    RES_SQL = SQL % (tableName, colName, colValues)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchone()
    if myresult is None:
        return True
    return False


    