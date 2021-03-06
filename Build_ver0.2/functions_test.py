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
    'foodName': 'ccc',
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
    exerciseInfo ={
        'exerciseName':'walk',
        'minute':60,
        'calorie':200,
    }

    def test_login(self):
        self.assertTrue(verify_login("gw@123.com","ggww"))

    # def test_register(self):
    #     self.assertFalse(verify_register("GW@gw.com","ggww"))


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
        userId = 'r@r.co'
        # mealdate = "2022-04-29"
        # mealdate = datetime.date(datetime.today())
        mealdate = "2022-05-01"
        data = get_deit_logs(userId, mealdate)
        print(data)
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

    def test_call_food_api(self):
        foodName = 'beef'
        data = call_food_API(foodName)
        print(data)

    # def test_update_meal_info(self):
    #     userId = self.mealdata['userId']
    #     data = update_meal_info(userId,self.mealdata)
    #     self.assertTrue(data)

    def test_get_fooodIdandName(self):
        data = get_fooodIdandName()
        print(data[0])
        print(data[0][0])
        self.assertTrue(len(data)>0)

    def test_format_food_detail(self):
        data = call_food_API('apple')
        print(data)
        self.assertTrue(len(data)>0)


    def test_give_recommandation(self):
        energy = 3000
        userId = 'GW'
        data = give_recommandation(userId, energy)
        print(data[0])
        self.assertTrue(len(data)>0)

    def test_get_exercise_logs(self):
        userId = 'GW'
        # date = datetime.strptime("2022-04-28", '%Y-%m-%d')
        date = datetime.now()
        data = get_exercise_logs(userId, date)
        print(data)
    
    # def test_delete_sport_info(self):
    #     id = 3
    #     data = delete_sport_info(id)
    #     self.assertTrue(data)
    # def test_update_exercise_info(self):
    #     userId = 'GW'
    #     data = update_exercise_info(userId, self.exerciseInfo)
    #     print(data)

    def test_give_advise(self):
        userId = 'root@root.com'
        date = datetime.date(datetime.today())
        # date = datetime.now()
        data = give_advise(userId, date)
        print(data)

"""
    ----------------unpassd test cases-------------------

"""

if __name__ == '__main__':
    unittest.main(exit=False)