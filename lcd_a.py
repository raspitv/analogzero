#!/usr/bin/python3
import lcddriver
from time import sleep, strftime
from datetime import datetime
from gpiozero import MCP3008

# LCD custom character variables
degree = chr(0)
squared = chr(1)
cust_chars = [[0x1c,0x14,0x1c,0x0,0x0,0x0,0x0,0x0],    # degree
             [0x8,0x14,0x8,0x10,0x1c,0x0,0x0,0x0]]     # squared      

deg = chr(176)+'C'       # this is for display on the terminal

lcd = lcddriver.lcd()    # create object for lcd control
lcd.lcd_load_custom_chars(cust_chars) # upload custom chars to LCD
lcd.lcd_clear()          # clear LCD ready for start

# display an intro message showing left/right/centre
lcd.lcd_display_string('{:^20}'.format("Hello Everyone!"), 1)
lcd.lcd_display_string('{:<20}'.format("I am a"), 2)
lcd.lcd_display_string('{:>20}'.format(("20x4 i"+squared+"c LCD")), 3)
lcd.lcd_display_string('{:^20}'.format("Running on a Pi"), 4)

sleep(3)
lcd.lcd_clear()

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

try:                   # now we're ready to start the main loop
    lcd.lcd_clear()
    counter = 0
    while True:        # correct time needs internet or RTC
        timenow = datetime.now().strftime('%b %d %H:%M:%S')
        timenow = '{:^20}'.format(timenow)   # < left, > right, ^ centre
        lcd.lcd_display_string(timenow, 1)
        inside = MCP3008(channel=0)
        outside = MCP3008(channel=1)
        in_ldr = MCP3008(channel=6)
        out_ldr = MCP3008(channel=7)
        in_temp = '{:.1f}'.format((3.3 * inside.value - 0.5) * 100)
        out_temp = '{:.1f}'.format((3.3 * outside.value - 0.5) * 100)
        in_light = str(int(in_ldr.value * 100))+'%'
        out_light = str(int(out_ldr.value * 100))+'%'
        print(in_temp, deg, 10 * ' ')
        print(out_temp, deg, 10 * ' ')
        print(in_light, 10 * ' ')
        print(out_light, 10 * ' ')
        lcd.lcd_display_string('{:^20}'.format(' In: '+in_temp+degree+'C '+in_light), 3)
        lcd.lcd_display_string('{:^20}'.format('Out: '+out_temp+degree+'C '+out_light), 4)      
        sleep(0.1)
       
finally:
    lcd.lcd_display_string(timenow, 1)
    lcd.lcd_display_string("switching off"+7*' ', 2)
    lcd.lcd_display_string("backlight in 2s", 3)

    sleep(5)
    lcd.lcd_display_string("      GOODBYE!      ", 4)
    lcd.backlight(0)   # swap 0 for 1 turns backlight on