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
lcd.lcd_display_string('{:^20}'.format("RasPiO Analog Zero"), 1)
lcd.lcd_display_string('{:^20}'.format("20x4 Weather Kit"), 2)
lcd.lcd_display_string('{:^20}'.format("Digi Thermometer"), 3)
lcd.lcd_display_string('{:^20}'.format("Voltmeter"), 4)
sleep(3)
lcd.lcd_clear()

def update():
    lcd.lcd_display_string('{:^20}'.format(row_one), 1)
    lcd.lcd_display_string('{:^20}'.format(row_two), 2)
    lcd.lcd_display_string('{:^20}'.format(row_three), 3)
    lcd.lcd_display_string('{:^20}'.format(row_four), 4)

# display a range of keyboard characters
lcd.lcd_display_string("ABCDEFGHIJKLMNOPQRST", 1)
lcd.lcd_display_string("UVWXYZabcdefghijklmn", 2)
lcd.lcd_display_string("opqrstuvwxyz{}[]'|?/", 3)
lcd.lcd_display_string("0123456789!@$%^&*()", 4)
sleep(1)

# activate every single pixel to test the display
pixel_test = chr(255) * 20
for x in range(1,5):
    lcd.lcd_display_string(pixel_test, x)
sleep(1)

row_one = "Making Custom Chars"
row_two = "on i"+squared+"c LCD "+degree+"C"
row_three = "is quite doable"
row_four = "if you need them"
update()
sleep(3)

lcd.lcd_display_string('{:<20}'.format("align left"), 1)
lcd.lcd_display_string('{:>20}'.format("align right"), 2)
lcd.lcd_display_string('{:<20}'.format("align left"), 3)
lcd.lcd_display_string('{:>20}'.format("align right"), 4)
sleep(3)

for x in range(1,5):
    lcd.lcd_display_string('{:^20}'.format("center"), x)
sleep(2)

try:                   # now we're ready to start the main loop
    lcd.lcd_clear()

    while True:        # correct time needs internet or RTC
        timenow = datetime.now().strftime('%b %d %H:%M:%S')
        row_one = timenow
        row_two = "RasPiO Analog Zero"
        row_three = "20x4 LCD Weather"
        row_four = "St'n/Therm/Voltmeter"
        update() 
        sleep(0.1)
       
finally:
    for x in range(5):
        timenow   = datetime.now().strftime('%b %d %H:%M:%S')
        row_one   = timenow
        row_two   = "Backlight is"
        row_three = "switching off in " + str(5-x) +"s"
        row_four  = "Bye"
        update()
        sleep(1)
    lcd.backlight(0)   # swap 0 for 1 turns backlight on