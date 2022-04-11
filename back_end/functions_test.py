from functions import *
from flask import json
from datetime import datetime
import unittest


class test_list_copy(unittest.TestCase):

    def test_login(self):
        self.assertTrue(verify_login("GW","ggww"))

    def test_register(self):
        self.assertFalse(verify_register("GW","ggww"))
    def test_update_user_info(self):
        info={
            
        'infoDate': date.today(),
        'userId':'GW',
        'userName': "a",
        'gender':'M',
        'allergySource': ['fish', 'soy'],
        'birthday':  datetime.strptime("1995-07-07", '%Y-%m-%d'),
        'height': 182,
        'weight': 103,
        'fatRate': 29,
        'isVegan': False,	
        'mealPlan': "keepHealth",
        }

        self.assertTrue(update_user_info("GW",info))


    """def test_get_user_info(self):
        data=get_user_info("GW",datetime.strptime("2022-04-11", '%Y-%m-%d'))
        self.assertTrue(len(data)>0)


    def test_get_user_logs(self):
        data=get_user_logs("GW")
        self.assertTrue(len(data)>0)"""

if __name__ == '__main__':
    unittest.main(exit=False)