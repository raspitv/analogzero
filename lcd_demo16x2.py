#!/usr/bin/python3
import lcddriver
from time import sleep, strftime
from datetime import datetime

# LCD custom character variables
degree  = chr(0)
squared = chr(1)
cust_chars = [[0x1c,0x14,0x1c,0x0,0x0,0x0,0x0,0x0],    # degree
             [0x8,0x14,0x8,0x10,0x1c,0x0,0x0,0x0]]     # squared      

deg = chr(176)+'C'       # this is for display on the terminal

lcd = lcddriver.lcd()    # create object for lcd control
lcd.lcd_load_custom_chars(cust_chars) # upload custom chars to LCD
lcd.lcd_clear()          # clear LCD ready for start

# display an intro message
lcd.lcd_display_string('{:^16}'.format("RasPiO Analog Zero"), 1)
lcd.lcd_display_string('{:^16}'.format("16x2 Weather Kit"), 2)

sleep(3)
lcd.lcd_clear()

def update():
    lcd.lcd_display_string('{:^16}'.format(row_one), 1)
    lcd.lcd_display_string('{:^16}'.format(row_two), 2)

# display a range of keyboard characters
lcd.lcd_display_string("ABCDEFGHIJKLMNOPQRST", 1)
lcd.lcd_display_string("UVWXYZabcdefghijklmn", 2)
sleep(1)

# activate every single pixel to test the display
pixel_test = chr(255) * 16
for x in range(1,3):
    lcd.lcd_display_string(pixel_test, x)
sleep(1)

row_one = "Make Custom Chars"
row_two = "on i"+squared+"c LCD "+degree+"C"
update()
sleep(3)

lcd.lcd_display_string('{:<16}'.format("align left"), 1)
lcd.lcd_display_string('{:>16}'.format("align right"), 2)
sleep(3)

for x in range(1,3):
    lcd.lcd_display_string('{:^16}'.format("center"), x)
sleep(2)

try:                   # now we're ready to start the main loop
    lcd.lcd_clear()

    while True:        # correct time needs internet or RTC
        timenow = datetime.now().strftime('%b %d %H:%M:%S')
        row_one = timenow
        row_two = "RasPiO Analog Zero"
        update() 
        sleep(0.1)
       
finally:
    for x in range(5):
        timenow   = datetime.now().strftime('%b %d %H:%M:%S')
        row_one   = timenow
        row_two = "switching off " + str(5-x) +"s"
        update()
        sleep(1)
    lcd.backlight(0)   # swap 0 for 1 turns backlight on