import pandas as pd
from datetime import datetime
class run:
    _user_data=None
    _food_data=None
    _user=None
    _daily_cal=0   
    def __init__(self,user=None):
        self._user_data=pd.read_csv('USER_INFO\\USER_BASE_INFO.CSV') 
        self._food_data=pd.read_csv('USER_INFO\\USER_LOGS.CSV')
        if user is not None:#  read the users info
            tar_info=self._user_data[self._user_data.name==user].sort_values(by="time").to_dict('index')
            tar_info=tar_info[list(tar_info.keys())[-1]]
            self._user=tar_info
            self._daily_cal=tar_info['daily_cal']

    def eat(self,foodname=None,calorie_rate=0,protein=0,carbohydrate=0,fat=0,weight=0,calcost=0,types=None):        
        if (foodname is not None) and (foodname in self._food_data.food_name.to_list()):
            tar_info=self._food_data[self._food_data.food_name==foodname].to_dict('index')
            tar_info=tar_info[list(tar_info.keys())[-1]]
            foodname=tar_info['food_name']
            calorie_rate=tar_info['calorie_rate']
            protein=tar_info['protein']
            carbohydrate=tar_info['carbohydrate']
            fat=tar_info['fat']    

            if (types is None ) or types not in ['B','BA','L','LA','D','DA']:
                types=input("please input the meal types('B','BA','L','LA','D','DA'):")
            if weight==0:
                weight=input("Please input the weight:")            
        else:
            foodname=input("please input food name:")            
            types=input("please input the meal types('B','BA','L','LA','D','DA'):")
            calorie_rate=input("please input food calorie_rate(per 100g):")      
            protein=input("please input food protein(per 100g):")      
            carbohydrate=input("please input food carbohydrate(per 100g):")      
            fat=input("please input food fat(per 100g):")      
            weight=input("please input food weight:")
        if calcost==0:
                calcost=int(weight)*int(calorie_rate)/100
        current_time = datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
        
        new_info=[len(self._food_data)+1,len(self._food_data)+1,foodname,self._user['name'],current_time,types,weight,calorie_rate,carbohydrate,protein,fat,calcost]
        ccc=self._food_data.columns.to_list()
        new_data=pd.DataFrame([new_info],columns=ccc)
        self._food_data=self._food_data.append(new_data)
        self._food_data.to_csv('USER_INFO\\USER_LOGS.CSV',index=False)       
        

trys=run(user="GW")
trys.eat("红烧肉")