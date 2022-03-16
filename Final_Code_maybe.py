import time
import RPi.GPIO as GPIO
import board
import threading
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
from w1thermsensor import W1ThermSensor
import sys
import lcd.Adafruit_ADS1x15.ADS1x15 as ADS
#from lcd.Adafruit_ADS1x15.analog_in import AnalogIn
import busio


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
#time.sleep(5)
buttonPin = 27
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(17, False)

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
i2c1 = board.I2C()  # uses board.SCL and board.SDA
i2c2 = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c2)
#channel = AnalogIn(ads, ADS.P0)

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c1, lcd_columns, lcd_rows)

sensor = W1ThermSensor()

lcd.clear()

def relayloop():
    while True:
        buttonState = GPIO.input(buttonPin)
    
        if buttonState == True:
            GPIO.output(17, False)
        else:
            GPIO.output(17, True)
            
def temploop():
    while True:
        temperature_c = round(sensor.get_temperature(),2)
        temperature_f = round((temperature_c * (9/5)) + 32,2)
        lcd.message = "The temperature \nis %s F" % temperature_f
        lcd.message = "The temperature \nis %s C" % temperature_c
        #v=round(channel.voltage,2)
        #ph = round((-5.641509*(v)) + 21.55509299,2)
        #lcd.message = "The pH is: " + str(ph)
        time.sleep(2)
        
    
thread1 = threading.Thread(target=relayloop)
thread1.start()

thread2 = threading.Thread(target=temploop)
thread2.start()
