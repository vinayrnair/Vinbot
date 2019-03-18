# Second iteration of controlling motors using RPi, L298n and DC Motors. The code is inspired by @Sentdex from Youtube
https://youtu.be/LlFkybEQFFA 
# This code assigns keyboard keys to the movements so that one can control using keyboard. This is an extension on Robot_1 code
#

import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(19, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    gpio.output(19, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    gpio.output(19, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    gpio.output(19, False )
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def right(tf):
    gpio.output(19, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def p_right(tf):
    gpio.output(19, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def p_left(tf):
    gpio.output(19, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()




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
    else :
        pass()

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
