#coding = utf-8
import RPi.GPIO as GPIO
import time


pin_4 = 4
pin_17 = 17
pin_23 = 23
pin_24 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)




def turnLedOn():
    GPIO.output(11,True)
    print('on')

def turnLedOff():
    GPIO.output(11,False)
    print('off')

def turnLedFlash():
    for i in range(1,10):
        GPIO.output(11, True)
        print('on')
        time.sleep(0.1)
        GPIO.output(11, False)
        print('off')
        time.sleep(0.1)


def motorInit():
    GPIO.setup(pin_4,GPIO.OUT)
    GPIO.setup(pin_17, GPIO.OUT)
    GPIO.setup(pin_23, GPIO.OUT)
    GPIO.setup(pin_24, GPIO.OUT)

def setStep(w1,w2,w3,w4):
    GPIO.output(pin_4,w1)
    GPIO.output(pin_17, w2)
    GPIO.output(pin_23, w3)
    GPIO.output(pin_24, w4)

def forward(delay):
    setStep(1,0,0,0)
    time.sleep(delay)
    setStep(0, 1, 0, 0)
    time.sleep(delay)
    setStep(0,0,1,0)
    time.sleep(delay)
    setStep(0,0,0,1)
    time.sleep(delay)