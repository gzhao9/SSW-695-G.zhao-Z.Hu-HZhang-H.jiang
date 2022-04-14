from functions import *
from flask import json
from datetime import datetime
from api import  app

print(json.loads(get_user_logs("GW"))[-1])


foodInfo = {
'foodName': 'bilibili',
'foodType': 'fruit',
'totalWeight': 20,
'protein': 1,
'fat':23,
'carbohydrate':6,
'energy':80,
'sugar':1.8,
'va':0,
'vc':200,
}
mealdata = {
    'Date':"2022-04-14",
    'foodId':3,
    'userId':'a@a.com', 
    'manuallyInput':'false',
    'mealType':'LA',
    'unit':251,
    'foodInfo':foodInfo,
    }

response = app.test_client().post(
    '/updateDietInfo/aaa@a.com', 
    data=json.dumps(mealdata),
    content_type='application/json',
)
data = response.get_data(as_text=True)
data=json.loads(data)
print(data)