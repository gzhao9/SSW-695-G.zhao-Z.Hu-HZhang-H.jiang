from api import app
from flask import json
import unittest
from datetime import datetime


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
            'Date':datetime.now(),
            'foodId':11,
            'userId':'a1@a.com', 
            'manuallyInput':'true',
            'mealType':'L',
            'unit':251,
            'foodInfo':foodInfo,
            }

        response = app.test_client().post(
            '/updateDietInfo/a2@a.com', 
            data=json.dumps(mealdata),
            content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data)==1)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)