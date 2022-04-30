from datetime import datetime
from connect_mydb import config
import mysql.connector
import json
from datetime import date
from datetime import datetime

mydb = mysql.connector.connect(**config)
mycursor = mydb.cursor(buffered=True)

def to_json(data):
    for i in range(len(data)):
        for k,v in data[i].items():
            if type(v)==type(date.today())or type(v)==type(datetime.now()):
                data[i][k]=v.strftime("%m-%d-%Y, %H:%M:%S")
    return json.dumps(data)
    # return data
# -----------------------------------build sql statement--------------------------------
def build_insert_SQL(tableName,datadict):
    columns = ', '.join("" + str(x).replace('/', '_') + "" for x in datadict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in datadict.values())
    sql = "INSERT INTO %s (%s) VALUES (%s);" % (tableName,columns,values)
    return sql
   

def build_single_search_SQL(tableName, colName,colValue):
    # if isinstance(colValue, str):
    #     sql = "select * from %s where %s = '%s' " % (tableName, colName, colValue)
    # elif isinstance(colValue, int) or isinstance(colValue, float):
    #     sql = "select * from %s where %s = %s " % (tableName, colName, colValue)
    # return sql
    if isinstance(colValue, int) or isinstance(colValue, float):
        sql = "select * from %s where %s = %s " % (tableName, colName, colValue)
    else:
        sql = "select * from %s where %s = '%s' " % (tableName, colName, colValue)
    return sql

def build_double_search_SQL(tableName, colName1, colValues1, colName2, colValues2):
    sql = "select * from %s where %s = '%s' and  %s = '%s'" % (tableName, colName1, colValues1,colName2, colValues2)
    return sql



def build_perticular_search_SQL(elementName, tableName, colName,colValue):
    if isinstance(colValue, str):
        sql = "select %s from %s where %s = '%s'" % (elementName, tableName, colName, colValue)
    elif isinstance(colValue, int) or isinstance(colValue, float):
        sql = "select %s from %s where %s = %s" % (elementName, tableName, colName, colValue)
    return sql

def build_delete_SQL(tableName, colName,colValue):
    if isinstance(colValue, str):
        sql = "delete from %s where %s = '%s';" % (tableName, colName, colValue)
    elif isinstance(colValue, int) or isinstance(colValue, float):
        sql = "delete from %s where %s = %s;" % (tableName, colName, colValue)
    return sql

def build_recommand_SQL(tableName, colName1, colValues1, colName2, colValues2):
    sql1 = "select * from %s where %s < %s and %s" % (tableName, colName1, colValues1, colName2)
    sql2 = " not like '%" + colValues2 + "%';"
    sql = sql1 + sql2
    return sql

def build_recommandAll_SQL(tableName, colName1, colValues1):
    sql = "select * from %s where %s < %s" % (tableName, colName1, colValues1)
    return sql


# ------------------------------find information----------------------
# find all data in table
def showTable(tableName):
    SQL = "select * from %s"
    RES_SQL = SQL % (tableName)
    mycursor.execute(RES_SQL)
    res_data = mycursor.fetchall()
    return res_data


def findId():
    SQL = "SELECT LAST_INSERT_ID();"
    mycursor.execute(SQL)
    res = mycursor.fetchone()
    return res

def showTwoCol(tableName, colName1, colName2):
    SQL = "select distinct %s, %s from %s"
    RES_SQL = SQL % (colName1,colName2,tableName)
    mycursor.execute(RES_SQL)
    res_data = mycursor.fetchall()
    return res_data


# find particular element in table
def findEleInTable(elementName,tableName,colName,colValue):
    RES_SQL = build_perticular_search_SQL(elementName, tableName, colName, colValue)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchall()
    return myresult

def findIfInTable(tableName,colName1, colValues1):
    RES_SQL = build_single_search_SQL(tableName, colName1, colValues1)
    mycursor.execute(RES_SQL)
    myresult = mycursor.fetchone()
    if myresult is None:
        return False
    return True



# find in table where key = colName, if exist, return True, else return false
def findIfInTableTwoEle(tableName,colName1, colValues1, colName2, colValues2):
    RES_SQL = build_double_search_SQL(tableName, colName1, colValues1, colName2, colValues2)
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
    field_names = [i[0] for i in mycursor.description]
    if len(myresult)>=1:
        result=list()
        for i in myresult:
            result.append(dict(zip(field_names,i)))
        #result=json.dumps(result)
    else:
        result=[{'isNone':True}]
    
    return to_json(result)
    

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
    field_names = [i[0] for i in mycursor.description]
    if len(myresult)>=1:
        result=list()
        for i in myresult:
            result.append(dict(zip(field_names,i)))
        #result=json.dumps(result)
    else:
        result=[{'isNone':True}]
    return to_json(result)



def recommandinTable(tableName, colName1, colValues1, colName2, colValues2):
    if colValues2 is None:
        RES_SQL = build_recommandAll_SQL(tableName, colName1, colValues1)
    else:
        RES_SQL = build_recommand_SQL(tableName, colName1, colValues1, colName2, colValues2)
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
    RES_SQL = build_insert_SQL(tableName, dataDict)
    try:
        mycursor.execute(RES_SQL)
        mydb.commit()
        return True
    except:
        mydb.rollback()
        return False

#
#
#
#
#
# -----------------------------delete information------------------------------
# delete one row in table
def deleteinTable(tableName,colName,colValues):
    still = findIfInTable(tableName, colName, colValues)
    if (not still):
        return False
    RES_SQL = build_delete_SQL(tableName, colName, colValues)
    try:
        mycursor.execute(RES_SQL)
        mydb.commit()
    except:
        mydb.rollback()
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

