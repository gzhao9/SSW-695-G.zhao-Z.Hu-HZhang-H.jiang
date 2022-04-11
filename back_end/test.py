from functions import *
from datetime import date
info={
	
'infoDate': date.today(),
'userId':'GW',
'userName': "a",
'gender':'M',
'allergySource': ['fish', 'soy'],
'birthday': "1997-04-07",
'height': 184,
'weight': 103,
'fatRate': 29,
'isVegan': False,	
'mealPlan': "keepHealth",
}

update_user_info("GW",info)