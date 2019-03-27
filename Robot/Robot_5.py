# Combines earlier Robot_1.py, Distance_1.py programs together.

import RPi.GPIO as gpio
import time
import sys
#import Tkinter as tk #uncomment this for manual controls


def init():
    gpio.setwarnings(False) #this is to remove any warning messages when the code is run
    gpio.setmode(gpio.BOARD) #in case BCM is used, then change the pin numbering accorindgly
    gpio.setup(19, gpio.OUT) # refer to gpio connections and breadboards and adapt
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(12, gpio.OUT) # this refers to hc-sr04 ultrasonic sensor connections
    gpio.setup(16, gpio.IN) # this refers to hc-sr04 ultrasonic sensor connections

# this section defines the movement of the rover
def stop(): #in case of manual control, please define all functions as e.g. stop(tf)
    gpio.output(19, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    print ("stop")
    #time.sleep(tf) #please uncomment these for manual control

def forward():
    gpio.output(19, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    print ("forward")
    #time.sleep(tf)

def reverse():
    gpio.output(19, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    print ("reverse")
    #time.sleep(tf)

def left():
    gpio.output(19, False )
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    print ("left")
    #time.sleep(tf)

def right():
    gpio.output(19, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    print ("right")
    #time.sleep(tf)

def p_right(): #this is to pivot right on the rover's own axis
    gpio.output(19, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    print ("Pivot right")
    #time.sleep(tf)

def p_left(): #this is to pivot right on the rover's own axis
    gpio.output(19, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    print ("Pivot left")
    #time.sleep(tf)

# this section is for manual controls
'''
def key_input(event):
    init()
    print ('key: '), event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() =='d':
        right(sleep_time)
    elif key_press.lower() == 'q':
        p_left(sleep_time)
    elif key_press.lower() == 'e':
        p_right(sleep_time)
    elif key_press.lower() == 'r':
        stop(sleep_time)
    else :
        pass

    gpio.cleanup()

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
'''

# this section is for object detecting auto-control
init()
stop()

#Check distance
while True:
    i = 0
    avgDistance = 0
    for i in range(5):
        gpio.output(12, False)
        time.sleep(0.1)

        gpio.output(12, True)
        time.sleep(0.00001)
        gpio.output(12, False)

        while gpio.input(16) == 0:
            pulse_start = time.time()

        while gpio.input(16) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)
        avgDistance = avgDistance + distance
    avgDistance = avgDistance / 5
    print (avgDistance)

# using avgDistance value to control motors
    flag = 0
    count = 0

    if avgDistance < 15:
        count = count + 1
        stop()
        time.sleep(1)
        reverse()
        time.sleep(1.5)
        if (count%3 == 1) & (flag == 0):
            right()
            flag=1
        else:
            left()
            flag=0
            time.sleep(1.5)
            stop()
            time.sleep(1)
    else:
        forward()
        flag=0
    
gpio.cleanup()
