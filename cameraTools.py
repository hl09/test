#coding = utf-8
import cv2
import datetime
import time


#使用opencv启动摄像头拍照，按时间命名保持图片
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
