#!/usr/bin/python3

#import RPi.GPIO as GPIO
import sys

try:
    import RPi.GPIO as GPIO
    import time
    import sched
except RuntimeError:
    print("error")
    sys.exit()
    
class Timechkr(object) 
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup()
s = sched.scheduler(time.time, time.sleep)
start_time = time.time

    def main():
        while True:
            s.enter(10, 1, check_time)
            print(s.queue)
            s.run()


    
    def check_time(s):
        current_time = time.time()
        difference = 60 - ((current_time - start_time) % 60)
        print('the time is ', current_time, difference,' minutes have gone past')
        
if __name__ == "__main__":
    main()
    

def main():
    i_tck = Timechker()
    while True:
       
