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


from numpy import linspace

#import VL53L1X
batch_temp = 60

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

    units = 'mm'
    
    def __init__(self):
        self.hydrometerRange = 146.0
        self.laserRange = 100.0
        hydrometer_brand = 'North Mountain Supply'
        hydrometer_scale = '0 to 100'
        self.increment = self.hydrometerRange / self.laserRange
        self.mm_to_abv = self.make_dict()

    
    def get_info(self):
        print("Brand: " + self.hydrometer_brand + " Scale: " + 
               self.hydrometer_scale)

    def set_hydrometerRange(self, new_value):
        if new_value != self.hydrometerRange:
            self.hydrometerRange = new_value
            self.mm_to_abv = self.make_dict()

    def set_laserRange(self, new_value):
        if new_value != self.laserRange:
            self.laserRange = new_value
            self.mm_to_abv = self.make_dict()

    
    #build dictionary that associates a height from the distance laser with an ABV.
    #uses equation in constructor to generate incremental values
    def make_dict(self):
        
        #make the key
        indices = range(0, int(self.laserRange))

        #for loop to fill y axis with increments for y(x)
        body = []
        sum = 0
        for index in range(len(indices)):
            body.append(round(sum,2))
            sum += self.increment
            # print(round(body[index],2), " ")

        return dict(zip(indices,body))


    def tempCorrection(batch_temp):

        #Given by manufacturer
        correction_factor = {
            55:-1.5, 
            60:0, 
            65:1.5, 
            70:5, 
            75:7, 
            80:8.5
        }

        index_len = len(correction_factor)

        #the correection factor in this range is effectively linear
        x_axis = numpy.linspace(55,80,(index_len*2))
        y_axis = numpy.linspace(-1.5,8.5, index_len*2)

        temp_coefficient = dict(zip(x_axis,y_axis))

        return temp_coefficient[batch_temp]


    def abvConversion(self,key,temp):
        return self.temp_Correction(temp) + self.mm_to_abv[key]
    
    def get_chart(self):
        for i in range(len(self.mm_to_abv)):
            print(self.mm_to_abv[i])


def main():
    testobj = abvScale()
    testobj.get_chart()
    #testobj.make_dict()

if __name__ == '__main__':
    main()