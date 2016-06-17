#!/usr/bin/python3
from gpiozero import MCP3008, LED
from time import sleep
red = LED(12)
ldr = MCP3008(channel=7)

while True:
    print("LDR: ", ldr.value)
    if ldr.value < 0.5:
        red.on()
        print ("LED on")
    else:
        red.off()
        print ("LED off")
    sleep(0.1)