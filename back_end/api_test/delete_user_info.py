from api import app
from flask import json
import unittest
from datetime import datetime


class test_list_copy(unittest.TestCase):

    def test_del_user_logs(self):
        response = app.test_client().post(
            '/delete_user_info', 
            data=json.dumps({
                'infoId':'37',
            }),
            content_type='application/json',
        )
        data = response.get_data(as_text=True)
        data=json.loads(data)

        self.assertTrue(response.status_code == 200)
        self.assertFalse(data["isSuccess"])
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)