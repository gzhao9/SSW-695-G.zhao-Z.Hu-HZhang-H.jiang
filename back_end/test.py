from functions import *
from datetime import date
info={
	
'infoDate': date.today(),
'userId':'GW',
'userName': "a",
'gender':'M',
'allergySource': ['fish', 'soy'],
'birthday':  datetime.strptime("1995-07-07", '%Y-%m-%d'),
'height': 182,
'weight': 103,
'fatRate': 29,
'isVegan': False,	
'mealPlan': "keepHealth",
}

print(update_user_info("GW",info))