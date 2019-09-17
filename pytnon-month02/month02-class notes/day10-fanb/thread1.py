'''
    thread
'''
import threading,os
from time import sleep

a = 1
#线程函数

def music():
    global a
    print('a>',a)
    a=1000
    for i in range(3):
        sleep(2)
        print(os.getpid(),'播放：千年等一回.mp3')

#创建线程对象
t = threading.Thread(target=music)
t.start()
#主线程执行
for i in range(4):
    sleep(1)
    print(os.getpid(),'主线程播放：那年明月.mp3')
t.join()

print('a=',a)