#!/usr/bin/python

#abvscale

from email.quoprimime import body_check
from importlib.resources import contents
from mmap import mmap
from re import L
import time
import signal
import sys
from turtle import rt


from numpy import interp

#import VL53L1X
batch_temp = 57

def rounded(temp, base = 5):
    tempRounded = base * round(temp/base)
    return tempRounded

def correctedTemperature(temp):
    temp = rounded(batch_temp)
    cf = correction_factor[(rounded(batch_temp))]
    print(temp + cf)
    return temp + cf

# correction factor based off temperatue correction chart that came with Hydrometer
# any ranged outside of this mean sensor fault or batch temperature is OoS
correction_factor = {
    55:-1.5, 
    60:0, 
    65:1.5, 
    70:5, 
    75:7, 
    80:8.5
}

class abvScale:

    VL53L1X_output = 'mm'
    
    def __init__(self):
        self.hydrometerRange = 146.0
        self.laserRange = 100.0
        hydrometer_brand = 'North Mountain Supply'
        hydrometer_scale = '0 to 100'
        increments = self.hydrometerRange / self.laserRange
    
    def get_info(self):
        print("Brand: " + self.hydrometer_brand + " Scale: " + 
               self.hydrometer_scale )

    def make_dict():
        #
        #psuedo code
        #for loop to fill x axis in dictionary with laser value 0 - 100
        #for loop to fill y axis with increments for y(x)
        #
        #

    def tempCorrection(batch_temp):
        #
        #pseudo code
        #obtain temperature from import temperatureProbe 
        #

    def abvConversion(key):

        # pseudo code
        #called by distance, use key to go from mm -> ABV
        #return dict[key] + tempCorrection

    

# for i in range(len(Indices)):
#     print (Indices[i])
#dict ABV = {}