#!/usr/bin/python

#abvscale

import time
import signal
import sys
from turtle import rt
from numpy import linspace

#import VL53L1X
#this is assuming the hydrometer is linear
#
temp = 60
class abvScale:

    units = 'mm'
    
    def __init__(self):
        self.hydrometerRange = 146 #mm measurement of the stem of the hydrometer
        hydrometer_brand = 'North Mountain Supply'
        hydrometer_scale = '0 to 100'
        self.laser_offset = 0
        self.laserRange = self.hydrometerRange - self.laser_offset
        self.increment = self.hydrometerRange / self.laserRange
        self.set_zero(self.laser_offset)
    
    #Originally meant to be setters/getters, but python doesn't use these
    #decorators should be used instead
    def set_zero(self,laser_reading):
        self.laser_offset = laser_reading
        self.mm_to_abv = self.make_dict()

    def get_info(self):
        print("Brand: " + self.hydrometer_brand + " Scale: " + 
               self.hydrometer_scale)
        
    def set_hydrometerRange(self, new_value):
        if new_value != self.hydrometerRange:
            self.hydrometerRange = new_value
            self.mm_to_abv = self.make_dict(self.laser_offset)

    def set_laserRange(self, new_value):
        if new_value != self.laserRange:
            self.laserRange = new_value
            self.mm_to_abv = self.make_dict(self.laser_offset)

    
    #build dictionary that associates a height from the distance laser with an ABV.
    #uses equation in constructor to generate incremental values
    def make_dict(self):

        #make the dictionary key
        indices = range(self.laser_offset, self.laserRange)

        #for loop to fill y axis with increments for y(x)
        body = []
        sum = 0
        for index in range(len(indices)):
            body.append(round(sum,2))
            sum += self.increment
            #print(round(body[index],2), " ")

        return dict(zip(indices,body))
    
    def get_chart(self,key):
        return self.mm_to_abv[key]


def main():
    current_scale = abvScale()
    return current_scale

if __name__ == '__main__':
    main()
