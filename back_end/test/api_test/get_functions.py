from api import app
from flask import json
import unittest
from datetime import datetime


class test_list_copy(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)