#coding = utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True :
    GPIO.output(11,True)
    print('on')
    time.sleep(0.1)
    GPIO.output(11,False)
    print('off')
    time.sleep(0.1)
