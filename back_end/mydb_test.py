import connect_mydb
mydb = connect_mydb.mydb
mycursor = mydb.cursor()
# mycursor.execute("INSERT INTO login (userId, userPassword) VALUES (%s, %s)", ("hu@jiang.com", "HJ"))
# mydb.commit()

# mycursor.execute("SELECT * FROM login")
# for f in mycursor:
#     print(f)

foodDict = {
        'foodId': 2015943,
        'foodName': "Cheddar cheese",
        'foodType': "cheese",
        'protein': 25.0,
        'fat':32.1,
        'carbohydrate':3.57,
        'energy':393,
        'sugar':0.0,
        'va':1070.0,
        'vc':0.0,
    }

# placeholders = ','.join(['%s'] * len(foodDict))
# cols = ','.join(foodDict.keys())
# SQL = "insert into %s (%s) values (%s);"
# RES_SQL = SQL % ("foodinfo", cols, placeholders)
# print('RES_SQL:'+RES_SQL)

# mycursor.execute(RES_SQL, list(foodDict.values()))

# mydb.commit()

# def selectRowFromTable(tableName,colName, colValues):
#     SQL = "select * from %s where %s = %s"
#     RES_SQL = SQL % (tableName, colName, colValues)
#     mycursor.execute(RES_SQL)
#     myresult = mycursor.fetchone()
#     if myresult is None:
#         return 0
#     return 1

def findIfInTable(tableName,colName, colValues):
    SQL = "select * from %s where %s = '%s'"
    RES_SQL = SQL % (tableName, colName, colValues)
    print(RES_SQL)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchone()
    if myresult is None:
        return False
    return True

username = 'gw@zhao.com'
password = '123456'
userInfo = {
        'userId': username,
        'userPassword': password
    }


# # a = findIfInTable("foodinfo", "foodId", 1)
# # print(a)
# cannotlogin = findIfInTable('login', 'userId', userInfo['userId'])

# print(cannotlogin)

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

insertLogin(userInfo)