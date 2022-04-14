from functions import *
from flask import json
from datetime import datetime

print(get_deit_logs("GW",datetime.strptime("2022-04-13", '%Y-%m-%d')))