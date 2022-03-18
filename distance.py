#!/usr/bin/env python

import numpy
import time
import sys
import signal
from collections import deque
from statistics import mean, stdev
import abvscale
import VL53L1X

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
tof.open()
tof.set_user_roi(VL53L1X.VL53L1xUserRoi(6,9,9,6))


# Optionally set an explicit timing budget
# These values are measurement time in microseconds,
# and inter-measurement time in milliseconds.
# If you uncomment the line below to set a budget you
# should use `tof.start_ranging(0)`
tof.set_timing(120000, 130)

deque_for_avg = deque([],10)

def initialize():
    tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
    tof.open()
    tof.set_user_roi(VL53L1X.VL53L1xUserRoi(6,9,9,6))
    scale = abvscale.main()
    tof.start_ranging(0)
    first_read = tof.get_distance()
    for _ in range(0,5):
        first_read = tof.get_distance()
    scale.set_zero(first_read)
    tof.stop_ranging()
    #print("Offset set to: ", scale.get_chart(first_read))
    return scale

def runLaser(scale):
    tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
    tof.open()
    tof.set_user_roi(VL53L1X.VL53L1xUserRoi(6,9,9,6)) #Center of SPAD array
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
    #signal.signal(signal.SIGINT, exit_handler)
    while running:
        distance_in_mm = tof.get_distance()
        if distance_in_mm > 0:
            deque_for_avg.appendleft(distance_in_mm)
        try:
            abv_no_temp = scale.abvConversion(numpy.mean(deque_for_avg))
        except KeyError:
            pass
        else:
            i += 1
        if i > 100:
            running = False
        time.sleep(0.05)


    return abv_no_temp


if __name__ == '__main__':
    runLaser()
