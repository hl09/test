#coding = utf-8
import RPi.GPIO as GPIO
import time


pin_5 = 5
pin_7 = 7
pin_11 = 11
pin_13 = 13



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


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
    GPIO.setup(pin_5,GPIO.OUT)
    GPIO.setup(pin_7, GPIO.OUT)
    GPIO.setup(pin_11, GPIO.OUT)
    GPIO.setup(pin_13, GPIO.OUT)

def setStep(w1,w2,w3,w4):
    GPIO.output(pin_5,w1)
    GPIO.output(pin_7, w2)
    GPIO.output(pin_11, w3)
    GPIO.output(pin_13, w4)

def forward(delay,steps):
    for i in range(0,steps):
      setStep(1,0,0,0)
      time.sleep(delay)
      setStep(0, 1, 0, 0)
      time.sleep(delay)
      setStep(0,0,1,0)
      time.sleep(delay)
      setStep(0,0,0,1)
      time.sleep(delay)


def checkDistince():
    GPIO.output(pin_11,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(pin_11,GPIO.LOW)

    while not GPIO.input(pin_13):
        pass

    t1 = time.time()


    while GPIO.input(pin_13):
        pass


    t2 = time.time()

    return (t2-t1)*340/2



def engineStart():
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.HIGH)
    print('engine start.....')


def engineOff():
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    print('engine off.....')



command = input('input your command:')
if command == 'engine start':
    for i in range(1,20):
      engineStart()
if command == 'engine off':
    engineOff()



'''
motorInit()
print('forward...')
forward(0.002,4096)



GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_11,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(pin_13,GPIO.IN)

time.sleep(2)

try:
    while True:
        print('Distince: %0.2f m'%checkDistince())
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
'''