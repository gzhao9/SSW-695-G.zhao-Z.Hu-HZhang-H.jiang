from datetime import datetime
from decimal import DivisionByZero


class food_log:
    _foodname=''
    _Calorie_rate=0
    _Calorie_cost=0
    _protein =0
    _carbohydrate=0
    _fat=0
    _weight=0
    def __init__(self,foodname='',calorie_rate=0,protein=0,carbohydrate=0,fat=0,weight=0,calcost=0,) -> None:
        self._foodname=foodname
        self._Calorie_rate=calorie_rate
        self._protein =protein
        self._carbohydrate=carbohydrate
        self._fat=fat
        self._weight=weight
        if calcost!=0:
            self._Calorie_cost=self._Calorie_rate*self.weight
        else:
            self._Calorie_cost=calcost
   #-------------------     
    def set_Calorie(self,Calorie=0):
        self._Calorie=Calorie
    
    def set_protein (self,protein =0):
        self._protein =protein 
    def set_carbohydrate(self,carbohydrate=0):
        self._carbohydrate=carbohydrate
    def set_fat(self,fat=0):
        self._fat=fat

    def set_Calorie_rate(self,Calorie_rate):
        self._Calorie_rate=Calorie_rate

    def set_Calorie_cost(self,Calorie_cost):
        self._Calorie_cost=Calorie_cost

    def set_weight(self,weight):
        self._weight=weight
    
#------------------
    def get_Calorie(self):
        return self._Calorie
    
    def get_protein (self):
        return self._protein
    def get_carbohydrate(self):
        return self._carbohydrate
    def get_fat(self,fat=0):
        return self._fat

    def get_Calorie_rate(self):
        return self._Calorie_rate

    def get_Calorie_cost(self):
        return self._Calorie_cost

    def get_weight(self):
        return self._weight


class sport_log:
    _sportname=''
    _Cal_burn_rate=0    #Calorie burn rate, cal/min
    _Calorie_cost=0
    _aerobic=True
    _time=0

    def __init__(self,soprtname='',Cal_burn_rate=0,aerobic=True,calcost=0,time=0):
        self._sportname=soprtname
        self._Cal_burn_rate=Cal_burn_rate    #Calorie burn rate, cal/min
        self._aerobic=aerobic
        self._time=time
        if calcost!=0:
            self._Calorie_cost=self._Calorie_rate*self.time
        else:
            self._Calorie_cost=calcost

    def set_Cal_burn_rate(self,Cal_burn_rate):   
        self._Cal_burn_rate=Cal_burn_rate
    def set_Calorie_cost(self,Calorie_cost):   
        self._Calorie_cost=Calorie_cost
    def set_aerobic(self,aerobic):  
        self._aerobic=aerobic
    def set_time(self,time):  
        self._time=time
#-----------------

    def get_Cal_burn_rate(self):   
        return self._Cal_burn_rate
    def get_Calorie_cost(self):   
        return self._Calorie_cost
    def get_aerobic(self):  
        return self._aerobic
    def get_time(self):  
        return self._time

class user:
    _username=''
    _hight=0
    _weight=0
    _fat_rate=0
    _age=0
    _gender=''
    _daily_cal=0
    def __init__(self,username='',hight=0,weight=0,fat_rate=0,age=0,gender=0,daily_cal=0) -> None:
        self._username=username
        self._hight=hight
        self._weight=weight
        self._fat_rate=fat_rate
        self._age=age
        self._gender=gender
        self._daily_cal=daily_cal
    def _creat_log(self):
        pass

    def read_log(self):
        pass
    #---------------------
    def set_username(self,username):
        self._username=username
    def set_hight(self,hight):
        self._hight=hight
    def set_weight(self,weight):
        self._weight=weight
    def set_fat_rate(self,fat_rate):
        self._fat_rate=fat_rate
    def set_age(self,age):
        self._age=age
    def set_gender(self,gender):
        self._gender=gender
    def set_daily_cal(self,daily_cal):
        self._daily_cal=daily_cal

    #--------------------
    def get_username(self):
        return self._username
    def get_hight(self):
        return self._hight
    def get_weight(self):
        return self._weight
    def get_fat_rate(self):
        return self._fat_rate
    def get_age(self):
        return self._age
    def get_gender(self):
        return self._gender
    def get_daily_cal(self):
        return self._daily_cal



class daily:
    _daily_cal=0   
    _date=datetime.today() 
    _protein =0
    _carbohydrate=0
    _fat=0
    def __init__(self,daily_cal=0,protein =0,carbohydrate=0,fat=0) -> None:
        self._daily_cal=daily_cal   
        self._protein =protein
        self._carbohydrate=carbohydrate
        self._fat=fat
    
    def eat(self,foodname='',calorie_rate=0,protein=0,carbohydrate=0,fat=0,weight=0,calcost=0,):
        food=food_log(foodname,calorie_rate,protein,carbohydrate,fat,weight,calcost)
        self._daily_cal-=food.get_Calorie()

    def sport(self,soprtname='',Cal_burn_rate=0,aerobic=True,calcost=0,time=0):  #
        sports=sport_log(soprtname,Cal_burn_rate,aerobic,calcost,time)
        self._daily_cal+=sports.get_Calorie_cost()

    def getinfo(self):
        pass

    def setinfo(self):
        pass
    
    def recoment(self):
        pass

    def save_log(self):
        pass
if __name__ == "__main__":
    pass