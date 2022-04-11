from api import app
from flask import json
import unittest
class test_list_copy(unittest.TestCase):
# -------------------Login and Register page---------------------------

    def test_verifyLogin(self):        
        response = app.test_client().post(
            '/verifyLogin',
            data=json.dumps({'userId': 'GW', 'password': "ggww"}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['isSuccess'] == True)

    def test_verifyRegister(self):        
        response = app.test_client().post(
            '/verifyRegister',
            data=json.dumps({'email': 'GW', 'password': "ggww"}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['isSuccess'] == False)

    #--------------------user info --------------------------
    def test_updateUserInfo(self):        
        response = app.test_client().post(
            '/updateUserInfo/GW',
            data=json.dumps({
                'allergySource':[],
                'birthday':"2022-04-10",
                'date':"2022-04-10",
                'fatRate':18,
                'fullName':"xxx",
                'gender':"male",
                'height':123,
                'isVegan':'false',
                'mealPlan':"keepHealth",
                'weight':1,
            }),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['isSuccess'] == True)

    def test_update_food(self):
        pass
    """def test_getUserInfo(self):        
        response = app.test_client().post(
            '/getUserInfo/GW',
            data=json.dumps({
                'date':"2022-04-10",
            }),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['isSuccess'] == True)

    def test_getUserInfo_logs(self):        
        response = app.test_client().post(
            '/getUserInfo_logs/GW',
            data=json.dumps({
                'date':"2022-04-10",
            }),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(data) >0)"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)