from functions import *
from flask import json
from datetime import datetime
from api import  app


response = app.test_client().post(
"/getAdvice/root@root.com", 
data=json.dumps({
        "date":"2022-04-01"
    }),
content_type='application/json',
)
data = response.get_data(as_text=True)
print(json.loads(data))