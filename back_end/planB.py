import csv
from email.contentmanager import raw_data_manager

def get_data(path):
    with open(path, mode='r') as inp:
        reader = csv.reader(inp)
        user_info = {rows[0]:rows[1] for rows in reader}
    return user_info

def csv_get_user_info(userId,date):
    raw=get_data("back_end\\database\\userInfo_logs.csv")
    result = [rows for rows in raw.values() if rows['userId']==userId and rows['infoDate']==date]
    return result
"""
def get_user_logs(userId):
    return flask_db_operate.findInTable(tableuserInfo, 'userId', userId)

def get_food_info(userId,foodId):
    return flask_db_operate.findInTableWithTwoLimit(tablefoodInfo, 'userId', userId, 'foodId', foodId)

def get_exercise_info(userId,sportId):
    return flask_db_operate.findInTableWithTwoLimit(tablesportInfo, 'userId', userId, 'sportId', sportId)

def get_deit_logs(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tablemealRecord, 'userId', userId, 'mealDate', date)

def get_exercise_logs(userId,date):
    return flask_db_operate.findInTableWithTwoLimit(tablesportRecord, 'userId', userId, 'sportDate', date)


#--------------------------update information-----------------------------
def update_user_info(userId,info):
    age=19
    info['userId']=userId
    info['BMR']=cal_BMR(info['gender'],info['weight'],info['height'],age)
    info['fatRate'] # calculation

    info['infoDate']=info.pop('date')
    info['userName']=info.pop('fullName')

    info['isVegan']=1 if info['isVegan']=='true' else 0

    return flask_db_operate.insertintoTable(tableuserInfo, info)

def update_food_info(userId,info):
    #store single food info
    #if '@' not in list(userID):#it from api or admin.
    #   set the comefrom as system
    #else: #from user, 
    #   set the comefrom as user
    #return foodID
    pass

def update_meal_info(userId,info):
    if info['manuallyInput']=='true':
        info['foodID']=update_food_info(userId,info['foodInfo'])
    #because when manuallyInput by user, the food info not in database, so it dose not have foodID. update_food_info(userId,info) will return the new foodID store in database.
    #del info['foodInfo']
    
    return flask_db_operate.updateinTable(tablemealRecord, info, 'userId', userId)

def update_exercise_info(userId,info):
    return flask_db_operate.updateinTable(tablesportRecord, info, 'userId', userId)


# --------------------------delete information----------------------------
def delete_user_info(infoId):
    return flask_db_operate.deleteinTable(tableuserInfo, 'infoId', infoId)

def delete_meal_info(mealId):
    return flask_db_operate.deleteinTable(tablemealRecord, 'mealRecordId',mealId)

def delete_sport_info(sportRecordId):
    return flask_db_operate.deleteinTable(tablesportRecord, 'sportRecordId',sportRecordId)
# -------------------------calculation function---------------------------
def cal_BMR(gender,weight,height,age):
    if gender.lower().startswith('m'):
        return 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        return 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
"""