#coding=utf8
import itchat

import test
import cameraTools
from itchat.content import *
import sys
import time

def turnOn():
    test.turnLedOn()
    print('turn on..')

def turnOff():
    test.turnLedOff()
    print('turn off..')

def turnFlash():
    test.turnLedFlash()
    print('turn flash..')

def engineStart():
    test.engineStart()

def engineOff():
    test.engineOff()

def photo():
    cameraTools.getPicture()

def video():
    cameraTools.getVideo()

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING,PICTURE])

def text_reply(msg):
    if msg['Text'] == 'turn on':
      itchat.send('%s: %s' % (msg['Type'], '执行指令'+msg['Text']), msg['FromUserName'])
      turnOn()

    if msg['Text'] == 'turn off':
      itchat.send('%s: %s' % (msg['Type'], '执行指令'+msg['Text']), msg['FromUserName'])
      turnOff()

    if msg['Text'] == 'turn flash':
      itchat.send('%s: %s' % (msg['Type'], '执行指令'+msg['Text']), msg['FromUserName'])
      turnFlash()

    if msg['Text'] == 'engine start':
      itchat.send('%s: %s' % (msg['Type'], '执行指令'+msg['Text']), msg['FromUserName'])
      engineStart()

    if msg['Text'] == 'engine off':
      itchat.send('%s: %s' % (msg['Type'], '执行指令'+msg['Text']), msg['FromUserName'])
      engineOff()

    #处理拍照指令，将拍照图片保存且发送给指令者
    if msg['Text'] == 'photo':
      itchat.send('%s: %s' % (msg['Type'], msg['Text'] + ' processed'), msg['FromUserName'])
      photo()
      print(sys.path[0] + "/a.jpg")
      itchat.send_image(sys.path[0] + "/a.jpg", msg['FromUserName'])



    if msg['Text'] == 'video':
      itchat.send('%s: %s' % (msg['Type'], msg['Text'] + ' processed'), msg['FromUserName'])
      video()
      print(sys.path[0] + "/myvideo.h264")
      itchat.send_file(sys.path[0] + "/myvideo.mp4", msg['FromUserName'])


    if msg['Text'] == 'water':
      itchat.send('%s: %s' % (msg['Type'], msg['Text'] + ' processed'), msg['FromUserName'])
      engineStart()
      time.sleep(8)
      photo()
      itchat.send_image(sys.path[0] + "/a.jpg", msg['FromUserName'])
      engineOff()



itchat.auto_login(True)
itchat.run()