#!/usr/bin/python3
from time import sleep
from gpiozero import MCP3008
import lcddriver
vref = 3.3
channels = [0,0,0,0,0,0,0,0]
temperatures = [0,0]
light_levels = [0,0]

lcd = lcddriver.lcd()    # create object for lcd control
lcd.lcd_clear()          # clear LCD ready for start

def update():
    lcd.lcd_display_string('{:^20}'.format(row_one), 1)
    lcd.lcd_display_string('{:^20}'.format(row_two), 2)
    lcd.lcd_display_string('{:^20}'.format(row_three), 3)
    lcd.lcd_display_string('{:^20}'.format(row_four), 4)

# display a centered intro message
row_one   = '{:^20}'.format("Hi. Enjoy using your")
row_two   = '{:^20}'.format("RasPiO Analog Zero")
row_three = '{:^20}'.format("20x4 Weather Station")
row_four  = '{:^20}'.format("Volt/thermometer Kit")
update()
sleep(3)

# Wiring instructions
#
# Wire up 2x TMP36 so the middle pins go to A0 and A1
# Wire up 2x LDR. One leg to 3V3 other leg to one end 
# of 10k resistor AND A6 or A7. 
# Other end of 10k resistor goes to GND

while True:
    for x in range(8):
        adc = MCP3008(channel=x)
        volts = 0.0
        for y in range(20):
            volts = volts + (vref * adc.value)
        volts = volts / 20.0
        if x < 2:
            temperatures[x] = '{:4.1f}'.format((volts - 0.5) * 100)
        if x > 5:
            light_levels[x-6] = '{:4.1f}'.format(volts / vref * 100)
        volts = '{:.3f}'.format(volts)            
        channels[x] = volts

# on-screen output useful for debug when tweaking
# shows the actual voltage at each analog input
        print("channel " + str(x) + ":", volts,"Volts")

# update the character LCD once every cycle then a short delay
        if x == 7:
            row_one   = "T0: " + temperatures[0] + "C"
            row_two   = "T1: " + temperatures[1] + "C"           
            row_three = "L0: " + light_levels[0] + "%"
            row_four  = "L1: " + light_levels[1] + "%"
            update()
        sleep(0.1)    # you can adjust refresh rate here