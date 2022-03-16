#!/usr/bin/python

#kombudroid main()

# #psuedo code
#     ask user if default
#     if yes run
#     if no   
#         get user input for parameters
#     obtain readings, use decorators?
#     check readings to alarm setpoints
#     if alarm setpoints passed activate LED
#     user resets system, setpoints are checked right away
#    
#     initialization:
#       distance,temp,pH 

from cmath import phase
import import_test
import runpy
import time
import alarmsys
import distance
import Final_Code_maybe


def check_readings(scale_obj):
    def obtain_readings():
        abv = distance.runLaser(scale_obj)
        temp = round(sensor.get_temperature(),2)
        pH = round(sensor.get_ph(),1)
        alarmsys.alarms(abv,temp,pH)
        return abv,temp,pH
    return obtain_readings()

def main():
    #zerod_scale = distance.initialize()
    # while running or buttonState == True:
    #     batch_info = check_readings(zerod_scale)
    #     curr_abv = batch_info[0]
    Final_Code_maybe()
    
    time.sleep(10)


if __name__=="__main__":
    main()