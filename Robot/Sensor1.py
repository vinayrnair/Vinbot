# First attempt of controlling ultrasonic sensor HC-SR04 using RPi. The code is inspired by @Sentdex from Youtube
https://youtu.be/LlFkybEQFFA 
# This code uses GPIO pins, 1k and 2k resistors on the breadboard to connect hc-sr04 to raspberry pi. This provides basic functionality of measuring distance
#


import RPi.GPIO as gpio
import time

#GPIO 12 is set for Trig and 16 for Echo
def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()

    while gpio.input(16) == 1:
        sig = time.time()

    tl = sig - nosig

    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('improper choice of measurement: in or cm')
        distance = None

    gpio.cleanup()
    gpio.setwarnings(False)

    return distance

print(distance('cm'))
