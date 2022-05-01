from functions import *
from flask import json
from datetime import datetime
from api import  app
#from fitness_tools.meals.meal_maker import MakeMeal
  
"""

# Cre
result=get_user_info("root@root.com","2022-04-29")

info=json.loads(get_user_logs('r@r.co'))[-1]
data=cal_info(58,170,24,'f',"buildMuscle")
print(info)

{'min_calories': 600, 'max_calories': 700, 'min_fat': 20.0, 'max_fat': 23.0, 'min_protein': 45.0, 'max_protein': 52.0, 'min_carbs': 60.0, 'max_carbs': 70.0, 'body_type': 'mesomorph'}
"""
# response = app.test_client().post(
# "/recomandationFoods/root@root.com", 
# data=json.dumps({
#         "date":"2022-04-01"
#     }),
# content_type='application/json',
# )
data = food_statistic()
print(data)
