# coding=utf8
import itchat

import test
import cameraTools
from itchat.content import *
import sys

import threading


def engineStart():
    test.engineStart()


def engineOff():
    test.engineOff()


def photo():
    cameraTools.getPicture()


def video():
    cameraTools.getVideo()


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE])
def text_reply(msg):
    if msg['Text'] == 'engine start':
        itchat.send('%s: %s' % (msg['Type'], msg['Text'] + ' processed'), msg['FromUserName'])
        engineStart()

    if msg['Text'] == 'engine off':
        itchat.send('%s: %s' % (msg['Type'], msg['Text'] + ' processed'), msg['FromUserName'])
        engineOff()

    # 处理拍照指令，将拍照图片保存且发送给指令者
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

        threads = []

        t1 = threading.Thread(target=video)
        threads.append(t1)
        t2 = threading.Thread(target=engineStart)
        threads.append(t2)

        for t in threads:
            t.setDaemon(True)
            t.start()

        for t in threads:
            t.join()

        engineOff()

        itchat.send_file(sys.path[0] + "/myvideo.mp4", msg['FromUserName'])

    if msg['Text'] == 'quit':
        itchat.send('%s: %s' % (msg['Type'], msg['Text'] + ' processed'), msg['FromUserName'])
        sys.exit()

    if msg['Text'] == 'commands':
        itchat.send_file(sys.path[0] + "/readme.txt", msg['FromUserName'])


if __name__ == '__main__':
    engineOff()

    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
