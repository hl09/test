#coding = utf-8

import datetime
import time
import pygame
import pygame.camera





def getPicture():
  pygame.init()
  pygame.camera.init()
  camera = pygame.camera.Camera("/dev/video0",(640,480))
  camera.start()
  imagetmp = camera.get_image()
  pygame.image.save(imagetmp,"a.jpg")
  print("get picture has been done")
  camera.stop()




getPicture()

