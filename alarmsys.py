<<<<<<< HEAD
#!usr/bin/python

class alarms():
    def __init__(self):
        self.ph_low = 2.5
        self.ph_high = 3.5
        self.abv_high = 2.0
        self.temp_low = 68
        self.temp_high = 78

    def turn_on_horn(self):
        print("noise")
        return False
    
    def check_readings(self,abv,ph,temp):
        if abv >= self.abv_high:
            print("High ABV detected")
            return self.turn_on_horn()
        if ph >= self.ph_high:
            print("High pH detected")
            return self.turn_on_horn()
        if ph <= self.ph_low:
            print("Low pH detected")
            return self.turn_on_horn()
        if temp >= self.temp_high:
            print("High Temp. detected")
            return self.turn_on_horn()
        if temp <= self.temp_low:
            print("Low Temp. detected")
            return self.turn_on_horn() 

=======
#!usr/bin/python

class alarms():
    def __init__(self):
        self.ph_low = 2.5
        self.ph_high = 3.5
        self.abv_high = 2.0
        self.temp_low = 68
        self.temp_high = 78

    def turn_on_horn(self):
        print("noise")
        return False
    
    def check_readings(self,abv,ph,temp):
        if abv >= self.abv_high:
            print("High ABV detected")
            return self.turn_on_horn()
        if ph >= self.ph_high:
            print("High pH detected")
            return self.turn_on_horn()
        if ph <= self.ph_low:
            print("Low pH detected")
            return self.turn_on_horn()
        if temp >= self.temp_high:
            print("High Temp. detected")
            return self.turn_on_horn()
        if temp <= self.temp_low:
            print("Low Temp. detected")
            return self.turn_on_horn() 

>>>>>>> 28ed83a7472090545024e2298e0cc481b02abe4a
