from functions import *
from flask import json
from datetime import datetime
import unittest
class test_list_copy(unittest.TestCase):

    def test_updateDiet_logs(self):
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
            'Date':"2022-04-13",
            'foodId':4,
            'userId':'GW', 
            'manuallyInput':'false',
            'mealType':'L',
            'unit':211,
            'foodInfo':foodInfo,
            }
        
        userId = mealdata['userId']
        res = update_meal_info(userId, mealdata)
        self.assertTrue(res)
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)