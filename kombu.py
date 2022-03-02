#!/usr/bin/python

#kombudroid main()

# #psuedo code
#     ask user if default
#     if yes run
#     if no   
#         get user input for parameters

#     run distance.py 

import import_test
import runpy
#import distance
import time
import alarmsys


def obtain_readings():
    #abv = distance.runLaser()
    temp = 0
    ph = 0
    # test readings against alarm setpoints 
    ala = alarmsys.alarms()
    running = ala.check_readings(abv,ph,temp)

running = True

def main():
    print(obtain_readings())

        # while running:
        #     obtain_readings()
        #     
        #     time.sleep(600)


if __name__=="__main__":
    main()