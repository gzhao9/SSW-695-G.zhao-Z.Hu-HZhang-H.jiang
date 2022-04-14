from api import app
from flask import json
import unittest
from datetime import datetime


class test_list_copy(unittest.TestCase):

 def test_verifyRegister(self):        
        response = app.test_client().post(
            '/verifyRegister',
            data=json.dumps({'userID': 'GW', 'password': "ggww"}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['isSuccess'] == False)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)