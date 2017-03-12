#coding=utf8
import itchat
import test
from itchat.content import *

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

def turnOn():
    test.turnLedOn()
    print('turn on..')

def turnOff():
    test.turnLedOff()
    print('turn off..')

def turnFlash():
    test.turnLedFlash()
    print('turn flash..')

itchat.auto_login(True)
itchat.run()