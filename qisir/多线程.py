#coding:utf-8

import threading
import time


def movie():
    print('now is moving'+str(time.time()))
    time.sleep(2)
    print('ending ....'+str(time.time()))

def music():
    print('now is musicing'+str(time.time()))
    time.sleep(3)
    print('ending ...'+str(time.time()))


if __name__ == '__main__':
    threads = []
    threads1 = threading.Thread(target = movie)
    threads.append(threads1)
    threads2 = threading.Thread(target = music)
    threads.append(threads2)

    for i in threads:
        i.setDaemon(True)
        i.start()

    for t in threads:
        t.join()

    print('结束'+str(time.time()))
    # movie()
    # music()

