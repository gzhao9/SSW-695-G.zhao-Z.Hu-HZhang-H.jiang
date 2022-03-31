from datetime import datetime

import connect_mydb
 
mydb = connect_mydb.mydb
mycursor = mydb.cursor()


# insert into foodInfo, if success, return true, else return false
def insertFood(foodDict):
    table = "foodInfo"
    placeholders = ','.join(['%s'] * len(foodDict))
    cols = ','.join(foodDict.keys())
    if not (findIfInTable(table, 'foodId', foodDict['foodId'])):
        SQL = "insert into %s (%s) values (%s);"
        RES_SQL = SQL % ("foodinfo", cols, placeholders)
        # print('RES_SQL:'+RES_SQL)
        mycursor.execute(RES_SQL, list(foodDict.values()))
        mydb.commit()
        return True
    else:
        return False


# find in table where id = colName, if exist, return True, else return false
def findIfInTable(tableName,colName, colValues):
    if isinstance(colValues, str):
        SQL = "select * from %s where %s = '%s'"
    elif isinstance(colValues, int) or isinstance(colValues, float):
        SQL = "select * from %s where %s = %s"
    else:
        SQL = "select * from %s where %s = '%s'"
    RES_SQL = SQL % (tableName, colName, colValues)
    print(RES_SQL)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchone()
    if myresult is None:
        return False
    return True


# insert into login table, if success, return true, else return false
def insertLogin(loginDict):
    table = "login"
    placeholders = ','.join(['%s'] * len(loginDict))
    cols = ','.join(loginDict.keys())
    if not findIfInTable(table, 'userId', loginDict['userId']):
        SQL = "insert into %s (%s) values (%s);"
        RES_SQL = SQL % (table, cols, placeholders)
        print(RES_SQL)
        # print('RES_SQL:'+RES_SQL)
        mycursor.execute(RES_SQL, list(loginDict.values()))
        mydb.commit()
        return True
    else:
        return False
