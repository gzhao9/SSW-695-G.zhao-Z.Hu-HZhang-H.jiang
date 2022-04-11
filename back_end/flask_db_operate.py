from datetime import datetime
from connect_mydb import config
import mysql.connector

mydb = mysql.connector.connect(**config)
mycursor = mydb.cursor()

# -----------------------------------build sql statement--------------------------------
def build_insert_SQL(tableName,datadict):
    columns = ', '.join("" + str(x).replace('/', '_') + "" for x in datadict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in datadict.values())
    sql = "INSERT INTO %s (%s) VALUES (%s);" % (tableName,columns,values)
    return sql
   

def build_single_search_SQL(tableName, colName,colValue):
    if isinstance(colValue, str):
        sql = "select * from %s where %s = '%s'" % (tableName, colName, colValue)
    elif isinstance(colValue, int) or isinstance(colValue, float):
        sql = "select * from %s where %s = %s" % (tableName, colName, colValue)
    return sql

def build_double_search_SQL(tableName, colName1, colValues1, colName2, colValues2):
    sql = "select * from %s where %s = '%s' and  %s = '%s'" % (tableName, colName1, colValues1,colName2, colValues2)
    return sql



def build_perticular_search_SQL(elementName, tableName, colName,colValue):
    if isinstance(colValue, str):
        sql = "select %s from %s where %s = '%s'" % (elementName, tablename, colName, colValue)
    elif isinstance(colValue, int) or isinstance(colValue, float):
        sql = "select %s from %s where %s = %s" % (elementName, tablename, colName, colValue)
    return sql
    

# ------------------------------find information----------------------
# find all data in table
def showTable(tableName):
    SQL = "select * from %s"
    RES_SQL = SQL % (tableName)
    mycursor.execute(RES_SQL)
    res_data = mycursor.fetchall()
    return res_data

# find particular element in table
def findEleInTable(elementName,tablename,colName,colValue):
    RES_SQL = build_perticular_search_SQL(elementName, tableName, colName, colValue)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchall()
    return myresult

# find in table where key = colName, if exist, return True, else return false
def findIfInTable(tableName,colName, colValue):
    RES_SQL = build_single_search_SQL(tableName, colName, colValue)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchone()
    if myresult is None:
        return False
    return True


# find in table where key = colName, return the result
def findInTable(tableName,colName, colValue):
    RES_SQL = build_single_search_SQL(tableName, colName, colValue)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchall()
    return myresult
    

# find in table with two limit
def findInTableWithTwoLimit(tableName, colName1, colValues1, colName2, colValues2):
    # if isinstance(colValues1, str) and isinstance(colValues2, str):
    #     SQL = "select * from %s where %s = '%s' and  %s = '%s'"
    # if (isinstance(colValues1, int) or isinstance(colValues1, float))and(isinstance(colValues2, int) or isinstance(colValues2, float)):
    #     SQL = "select * from %s where %s = %s and %s = %s"
    # SQL = "select * from %s where %s = %s and %s = %s"
    RES_SQL = build_double_search_SQL(tableName, colName1, colValues1, colName2, colValues2)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchall()
    return myresult
#
#
#
#
#
# -----------------------------insert information------------------------------
# insert into login table, if success, return true, else return false
def insertintoTable(tableName,dataDict):
    if not findIfInTable(tableName, 'userId', dataDict['userId']):
        RES_SQL = build_insert_SQL(tableName, dataDict)
        mycursor.execute(RES_SQL)
        mydb.commit()
        return True
    else:
        return False

#
#
#
#
#
# -----------------------------delete information------------------------------
# delete one row in table
def deleteinTable(tableName,colName,colValues):
    if isinstance(colValues, str):
        SQL = "delete from %s where %s = '%s'"
    if isinstance(colValues, int) or isinstance(colValues, float):
        SQL = "delete from %s where %s = %s"
    RES_SQL = SQL % (tableName, colName, colValues)
    print(RES_SQL)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchone()
    mydb.commit()
    if myresult is None:
        return False
    return True

#
#
#
#
#
#----------------------------update information---------------------------------
# update perticular infomation in table
def updateinTable(tableName,dataDict,colName,colValues):
    placeholders = ','.join('{}=%s'.format(k) for k in dataDict)
    operate = "update %s " % tableName
    SQL ="set {}".format(placeholders)
    limit = " where %s = '%s' " % (colName, colValues)
    RES_SQL = operate + SQL + limit
    val = formatSQL(dataDict)
    strs=RES_SQL % tuple(val)
    mycursor.execute(RES_SQL, tuple(val))
    #mycursor.fetchone()
    myresult = mycursor.fetchall()
    if myresult == []:
        return False
    return myresult


def formatSQL(dataDict):
    val = list()
    for value in dataDict.values():
        if type(value) == str:
            val.append(f"'{value}'")
        elif type(value) == list:
            val.append(f"'{','.join(value)}'")
        else:
            val.append(value)
    return val




# # insert into foodInfo, if success, return true, else return false
# def insertFood(foodDict):
#     table = "foodInfo"
#     placeholders = ','.join(['%s'] * len(foodDict))
#     cols = ','.join(foodDict.keys())
#     if not (findIfInTable(table, 'foodId', foodDict['foodId'])):
#         SQL = "insert into %s (%s) values (%s);"
#         RES_SQL = SQL % (table, cols, placeholders)
#         # print('RES_SQL:'+RES_SQL)
#         mycursor.execute(RES_SQL, list(foodDict.values()))
#         mydb.commit()
#         return True
#     else:
#         return False

# # insert into userinfo table, if success, return true, else return false
# def insertUserInfo(userInfoDict):
#     table = "userInfo_logs"
#     placeholders = ','.join(['%s'] * len(userInfoDict))
#     cols = ','.join(userInfoDict.keys())
#     if not findIfInTable(table, 'userId', userInfoDict['userId']):
#         SQL = "insert into %s (%s) values (%s);"
#         RES_SQL = SQL % (table, cols, placeholders)
#         print(RES_SQL)
#         # print('RES_SQL:'+RES_SQL)
#         mycursor.execute(RES_SQL, list(userInfoDict.values()))
#         mydb.commit()
#         return True
#     else:
#         return False


# # insert into meal record table, if success, return true, else return false
# def insertMealRecord(mealDict):
#     table = "mealRecord"
#     placeholders = ','.join(['%s'] * len(mealDict))
#     cols = ','.join(mealDict.keys())
#     if True:
#         SQL = "insert into %s (%s) values (%s);"
#         RES_SQL = SQL % (table, cols, placeholders)
#         print(RES_SQL)
#         mycursor.execute(RES_SQL, list(mealDict.values()))
#         mydb.commit()
#         return True
#     else:
#         return False
