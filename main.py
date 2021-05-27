#from mac
import time as sleep
import tm1637 as DSPSEG
import drivers as DSPLCD
import adafruit_mlx90614 as MLX
import board

#test from mac
dip = "sample_sss"

segmentDisplay = DSPSEG.TM1637(clk=4, dio=17)
tempSensor = MLX.MLX90614(board.I2C())

def i2c_lcd(temperature):
    lcdDisplay = DSPLCD.lcd()
    lcdDisplay.lcd_display_string("=TEMPERATURE=", 1)  # Write line of text to first line of display
    lcdDisplay.lcd_display_string(str(temperature), 2)  # Write line of text to second line of display


while 1:
    temperature = tempSensor.object_temperature
    segmentDisplay.temperature(temperature)
    i2c_lcd(temperature)
    sleep(1)
