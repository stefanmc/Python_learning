#coding:utf-8

import threading
from time import ctime,sleep


def movie():
    print('now is moving'+str(ctime()))
    sleep(2)
    print('ending ....'+str(ctime()))

def music():
    print('now is musicing'+str(ctime()))
    sleep(3)
    print('ending ...'+str(ctime()))

#
# if __name__ == '__main__':
#     threads = []
#     threads1 = threading.Thread(target = movie)
#     threads.append(threads1)
#     threads2 = threading.Thread(target = music)
#     threads.append(threads2)
#
#     for i in threads:
#         i.setDaemon(True)
#         i.start()
#
#     for t in threads:
#         t.join()
#
#     print('结束'+str(ctime()))
#     # movie()
#     # music()


