import RPi.GPIO as GPIO
import time


def turn_on(color):
    GPIO.output(color, GPIO.HIGH)
    time.sleep(1)

def turn_off(color):
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

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)

    for i in range(0, 20):
        turn_off(RED)
        turn_off(GREEN)
        turn_off(BLUE)

    GPIO.cleanup()

if __name__ == '__main__':
    main()



