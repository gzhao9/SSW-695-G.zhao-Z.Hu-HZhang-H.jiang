from api import app
from flask import json
import unittest
from datetime import datetime
class test_list_copy(unittest.TestCase):
# -------------------Login and Register page---------------------------
    
    # def test_verifyLogin(self):        
    #     response = app.test_client().post(
    #         '/verifyLogin',
    #         data=json.dumps({'userID': 'GW', 'password': "ggww"}),
    #         content_type='application/json',
    #     )

    #     data = json.loads(response.get_data(as_text=True))

    #     self.assertTrue(response.status_code == 200)
    #     self.assertTrue(data['isSuccess'] == True)

    # def test_verifyRegister(self):        
    #     response = app.test_client().post(
    #         '/verifyRegister',
    #         data=json.dumps({'userID': 'GW', 'password': "ggww"}),
    #         content_type='application/json',
    #     )

    #     data = json.loads(response.get_data(as_text=True))

    #     self.assertTrue(response.status_code == 200)
    #     self.assertTrue(data['isSuccess'] == False)

    #--------------------user info --------------------------
    def test_getUserInfo_logs(self):
        response = app.test_client().post(
            '/getUserInfo_logs/GW', content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)

        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data))

    def test_get_last_UserInfo(self):
        response = app.test_client().post(
            '/get_last_UserInfo/GW', content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)

        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data))
    def test_getUserInfo(self):        
        response = app.test_client().post(
            '/getUserInfo/GW',
            data=json.dumps({
                'date':"2022-04-12",
            }),
            content_type='application/json',
        )

        data = response.get_data(as_text=True)
        data=json.loads(data)

        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data) >0)

    # def test_del_user_logs(self):
    #     response = app.test_client().post(
    #         '/delete_user_info', 
    #         data=json.dumps({
    #             'infoId':'37',
    #         }),
    #         content_type='application/json',
    #     )
    #     data = response.get_data(as_text=True)
    #     data=json.loads(data)

    #     self.assertTrue(response.status_code == 200)
    #     self.assertFalse(data["isSuccess"])

    #----diet-------
    def test_getDietlogs(self):
        response = app.test_client().post(
            '/getDietLogs/h1@123.com', 
            data=json.dumps({
                'date':'2022-04-12',
            }),
            content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data)==1)

    def test_getExerciseLogs(self):
        response = app.test_client().post(
            '/getExerciseLogs/hy@zhang.com', 
            data=json.dumps({
                'date':'2022-04-02',
            }),
            content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data)==1)

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
            'userId':'a@a.com', 
            'manuallyInput':'true',
            'mealType':'L',
            'unit':251,
            'foodInfo':foodInfo,
            }

        response = app.test_client().post(
            '/updateDietInfo/a@a.com', 
            data=json.dumps(mealdata),
            content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data)==1)

    def test_give_the_advise(self):
        timedata = {
            'date':"2022-05-01",
        }
        response = app.test_client().post(
            '/give_advise/root@root.com', 
            data=json.dumps(timedata),
            content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data)>=1)



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)