from functions import *
from datetime import date
from flask_db_operate import *
info={
	
'infoDate': date.today(),
'userId':'GWW',
'userName': "a",
'gender':'M',
'allergySource': ['fish', 'soy'],
'birthday':  datetime.strptime("1997-10-07", '%Y-%m-%d'),
'height': 182,
'weight': 103,
'fatRate': 29,
'isVegan': False,	
'mealPlan': "keepHealth",
'BMR': 1000,
}

# print(update_user_info("GW",info))

# insertintoTable('userInfo_logs',info)4

# update_user_info('GWW', info)

delete_user_info(6)