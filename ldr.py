#!/usr/bin/python3
from gpiozero import MCP3008
from time import sleep

while True:
    for x in range(0, 8):
        with MCP3008(channel=x) as reading:
            print(x,": ", reading.value)
    sleep(0.1)