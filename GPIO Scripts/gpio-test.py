#!/usr/bin/python3

import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
    import time
    import sys

except RuntimeError:
    print("error")

    
GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()
print(mode)

GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
x = 0
time.sleep(1)
while(x<1):
    GPIO.output(11, True)
    time.sleep(1)
    GPIO.output(11, False)
    print('wait1 done')
    GPIO.output(13, True)
    time.sleep(1)
    GPIO.output(13, False)
    print('wait2 done')
    GPIO.output(15, True)
    time.sleep(1)
    GPIO.output(15, False)
    print('wait3 done')
    x+=1
    
GPIO.cleanup()
print('program executed')
sys.exit()
    
