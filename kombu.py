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
import distance

def main():
    
    userIn = input("Use default settings? [Y/N]: ")
    print(userIn)

    # if (userIn == 'N' or 'n'):
    #         #ask input variables
    #         print("wtf")
    if(userIn == 'Y' or 'y'):
        import_test.test()
        distance.runLaser()

if __name__=="__main__":
    main()