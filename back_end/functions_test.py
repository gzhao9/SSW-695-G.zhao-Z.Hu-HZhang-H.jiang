from functions import *
from flask import json
from datetime import datetime
import unittest


class test_list_copy(unittest.TestCase):
    info={
            
        'date': datetime.now(),
        'userId':"GW",
        'fullName': "a",
        'gender':'M',
        'allergySource': 'fish, soy',
        'birthday':  datetime.strptime("1995-07-07", '%Y-%m-%d'),
        'height': 182,
        'weight': 103,
        'fatRate': 29,
        'isVegan': False,	
        'mealPlan': "keepHealth",
        }

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
        'userId':'h1@123.com', 
        'manuallyInput':'true',
        'mealType':'L',
        'unit':251,
        'foodInfo':foodInfo,
        }

    def test_login(self):
        self.assertTrue(verify_login("GW","ggww"))

    def test_register(self):
        self.assertFalse(verify_register("GW","ggww"))


    # def test_update_user_info(self):
    #     self.assertTrue(update_user_info(self.info['userId'],self.info))

    def test_get_user_info(self):
        data=get_user_info("GW",datetime.strptime("2022-04-12", '%Y-%m-%d'))
        print(type(data))
        # data=get_user_info("GW","2022-04-12")
        self.assertTrue(len(data)>0)
    
    def test_get_user_logs(self):
        data=get_user_logs("GW")
        self.assertTrue(len(data)>0)

    def test_get_food_info(self):
        comefrom = 'webapi'
        foodId = 1886337
        data = get_food_info(comefrom, foodId)
        self.assertTrue(len(data)>0)

    def test_get_exercise_info(self):
        sportId = 1
        data = get_exercise_info(sportId)
        self.assertTrue(len(data)>0)

    def test_get_deit_logs(self):
        # userId = self.info['userId']
        userId = 'h1@123.com'
        mealdate = datetime.strptime("2022-04-12", '%Y-%m-%d')
        data = get_deit_logs(userId, mealdate)
        print(type(data))
        self.assertTrue(len(data)>0)

    def test_get_exercise_logs(self):
        userId = 'GW'
        sportdate = datetime.strptime("2022-04-1", '%Y-%m-%d')
        data = get_exercise_logs(userId, sportdate)
        self.assertTrue(len(data)>0)


    def test_get_infoId(self):
        userId = 'GW'
        data = get_infoId(userId)
        self.assertTrue(len(data)>0)
    
    # def test_delete_user_info(self):
    #     infoId = 35
    #     res = delete_user_info(infoId)
    #     self.assertTrue(res)


    # def test_delete_meal_info(self):
    #     mealRecordId = 5
    #     res=delete_meal_info(mealRecordId)
    #     self.assertTrue(res)
        
    def test_get_infoIdandfrom(self):
        data = get_infoIdandfrom()
        self.assertTrue(len(data)>0)
        
    # def test_update_food_info(self):
    #     userId = 'GW'
    #     data = update_food_info(us erId,self.foodInfo)
    #     self.assertTrue(data == 9)

    # def test_update_meal_info(self):
    #     userId = self.mealdata['userId']
    #     data = update_meal_info(userId,self.mealdata)
    #     self.assertTrue(data)

    def test_get_fooodIdandName(self):
        data = get_fooodIdandName()
        self.assertTrue(len(data)>0)

"""
    ----------------unpassd test cases-------------------




"""

if __name__ == '__main__':
    unittest.main(exit=False)