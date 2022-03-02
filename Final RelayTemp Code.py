import time
import RPi.GPIO as GPIO
import board
import threading
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
from w1thermsensor import W1ThermSensor

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
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

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
        
    
thread1 = threading.Thread(target=relayloop)
thread1.start()

thread2 = threading.Thread(target=temploop)
thread2.start()