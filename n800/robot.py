#!/usr/bin/env python
'''
Provides a serial connection abstraction layer
for use with Arduino "MultipleServos" sketch.
'''
import sys
import time

import serial

usbport = '/dev/tty.usbserial-A6008bB7'
#ser = serial.Serial(usbport, 9600, timeout=1)

def move(direction):
    '''Moves the robot in the direction.

    Arguments:
        direction
          the desired direction, an integer from 0 to 180

    (e.g.) >>> servo.move('F')
           ... # "move robot forward"'''

    direction = direction.upper()
    if direction in ('F', 'B', 'L', 'R'):
        #ser.write(direction)
        pass
    else:
        print "Must inform valid direction:"
        print "      L for left"
        print "      R for right"
        print "      F for forward"
        print "      B for backward"

def run(d, tm):
    while True:
        move(d)
        time.sleep(tm)
