#!/usr/bin/env python

import time
import sys
import signal

import VL53L1X


#def runLaser():
print("""distance.py

Display the distance read from the sensor.

Uses the "Short Range" timing budget by default.

Press Ctrl+C to exit.

""")


# Open and start the VL53L1X sensor.
# If you've previously used change-address.py then you
# should use the new i2c address here.
# If you're using a software i2c bus (ie: HyperPixel4) then
# you should `ls /dev/i2c-*` and use the relevant bus number.
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.set_user_roi(VL53L1X.VL53L1xUserRoi(6,9,9,6))
tof.open()

# Optionally set an explicit timing budget
# These values are measurement time in microseconds,
# and inter-measurement time in milliseconds.
# If you uncomment the line below to set a budget you
# should use `tof.start_ranging(0)`
tof.set_timing(120000, 130)

tof.start_ranging(0)  # Start ranging
                      # 0 = Unchanged
                      # 1 = Short Range
                      # 2 = Medium Range
                      # 3 = Long Range


running = True


def exit_handler(signal, frame):
    global running
    running = False
    tof.stop_ranging()
    print()
    sys.exit(0)


# Attach a signal handler to catch SIGINT (Ctrl+C) and exit gracefully
signal.signal(signal.SIGINT, exit_handler)

while running:
    distance_in_mm = tof.get_distance()
    #abv_temp_corrected = abvScale.abvConversion(distance_in_mm, 60)
    print("Distance: {}mm".format(distance_in_mm))
    time.sleep(0.05)

#if __name__ == '__main__':
#   runLaser()
