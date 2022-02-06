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

GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
print('should be off')
time.sleep(15)
x=0
print('test')
while(x<1):
    GPIO.output(11, True)
    print('pin active')
    time.sleep(30)
    x+=1

print('test complete')