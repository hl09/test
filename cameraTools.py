
import picamera
import os


def getPicture():
  if os.path.exists("a.jpg"):
    os.remove("a.jpg")

  camera = picamera.PiCamera()
  camera.capture('a.jpg')
  camera.close()


def getVideo():
    if os.path.exists('myvideo.h264'):
      os.remove('myvideo.h264')

    if os.path.exists('myvideo.mp4'):
      os.remove('myvideo.mp4')

    camera = picamera.PiCamera()
    camera.resolution = (1024,768)

    camera.start_preview()
    camera.start_recording('myvideo.h264')
    camera.wait_recording(8)
    camera.stop_recording()
    camera.close()

    os.system("MP4Box -add myvideo.h264 myvideo.mp4")

