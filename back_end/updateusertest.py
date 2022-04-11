from api import app
from flask import json
import unittest
from functions import update_user_info
class test_list_copy(unittest.TestCase):

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
    def test_update_user_info(self):
        info = {
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
        }
        userId = 'GW'
        res = update_user_info(userId, info)
        self.assertTrue(res)
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)