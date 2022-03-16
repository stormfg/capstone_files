if (temperature_c < 18 or temperature_c > 28)
    lcd.message = "The temperature is " + temperature_c
    GPIO.output(22, True)
    time.sleep(5):
    GPIO.output(22, False)
    lcd.clear()
if (ph < 2.0 or ph > 4.0)
    lcd.message = "The pH is " + ph
    GPIO.output(22, True)
    time.sleep(5):
    GPIO.output(22, False)
    lcd.clear()
if (abv < 1.5)
    lcd.message = "The abv is " + abv
    GPIO.output(22, True)
    time.sleep(5):
    GPIO.output(22, False)
    lcd.clear()
