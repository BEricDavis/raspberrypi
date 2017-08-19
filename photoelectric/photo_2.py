#!/usr/bin/env python
# Turn an LED off and on based on the brightness detected by the light sensor.
# We're actually measuring the time it takes for the capacitor to charge.

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

def turn_on(color):
    GPIO.output(color, GPIO.HIGH)

def turn_off(color):
    GPIO.output(color, GPIO.LOW)

def main():

    RED = 12 
    GPIO.setup(RED, GPIO.OUT)

    while True:
        level = RCtime(11)

        print(level)
        if level > 2500:
            turn_on(RED)
        else:
            turn_off(RED)

if __name__ == '__main__':
    main()


