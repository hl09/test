import threading

from time import sleep, ctime


def test123():
    for i in range(2):
        print ('123: ' + str(ctime()))
        sleep(1)


def test456():
    for i in range(2):
        print ('456: ' + str(ctime()))
        sleep(1)



threads = []

t1 = threading.Thread(target=test123)
threads.append(t1)
t2 = threading.Thread(target=test456)
threads.append(t2)


if __name__ == '__main__':

    for t in threads:
        t.setDaemon(True)
        t.start()
