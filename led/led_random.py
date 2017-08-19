import RPi.GPIO as GPIO
import time
import random


def turn_on(color):
    print('Turning {} ON'.format(color))
    GPIO.output(color, GPIO.HIGH)
    time.sleep(1)

def turn_off(color):
    print('Turning {} OFF'.format(color))
    GPIO.output(color, GPIO.LOW)
    time.sleep(1)

def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(25)
    return

def main():
    # use the board pin numbers
    GPIO.setmode(GPIO.BOARD)

    RED = 12
    GREEN = 16
    BLUE = 18

    color_list = (RED, GREEN, BLUE)
    states = (turn_on, turn_off)

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)

    while True:
        state = random.choice(states)
        color = random.choice(color_list)
        state(color)
        

    GPIO.cleanup()

if __name__ == '__main__':
    main()



