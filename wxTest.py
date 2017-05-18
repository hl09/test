#coding=utf8
import itchat
import test
import cameraTools
from itchat.content import *
import sys


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
    cameraTools.capturePicture()

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
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

    if msg['Text'] == 'photo':
      itchat.send('%s: %s' % (msg['Type'], '执行指令'+msg['Text']), msg['FromUserName'])
      photo()
      itchat.send_image(sys.path[0]+'\aa.png',msg['FromUserName'])



itchat.auto_login(True)
itchat.run()