#!usr/bin/python

import numpy

batch_temp = 59

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
def tempCorrection():

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
    array_size = 2*index_len
    y_increment = abs(-1.5/8.5)
    #the correction factor in this range is effectively linear
    x_axis = numpy.linspace(55,80,(array_size),dtype=int)
    y_axis = numpy.linspace(-1.5,8.5,array_size)
    print(x_axis)
    temp_coefficient = dict(zip(x_axis,y_axis))
    print(temp_coefficient)
    #return temp_coefficient[batch_temp]

def main():
    tempCorrection()
if __name__ =='__main__':
    main()