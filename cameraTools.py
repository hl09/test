#coding = utf-8
import cv2
import datetime
import time
import os
import os.path
import sys


def capturePicture():
  cap = cv2.VideoCapture(0)
  ret,frame = cap.read()
  time.localtime(time.time())
  now = datetime.datetime.now()
  filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '-'+ str(now.second)+ '-' + str(now.microsecond)  + '.png'
  print(filename)
  filename = 'aa.png'
  cv2.imwrite(filename,frame)
  cap.release()
  cv2.destroyAllWindows()
