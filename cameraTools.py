#coding = utf-8

import datetime
from time import sleep
import picamera




def getPicture():
  camera = picamera.PiCamera()
  camera.capture('a.jpg')
  camera.start_preview()


def getVideo():
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.start_recording('video.h264')
    sleep(6)
    camera.stop_recording()

getPicture()

getVideo()