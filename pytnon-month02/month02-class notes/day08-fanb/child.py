#处理僵尸进程
from time import  sleep
import os

def f1():
    for i in range(3):
        sleep(2)
        print('写代码')

def f2():
    for i in range(2):
        sleep(4)
        print('测代码')


pid = os.fork()
if pid == 0:
    print('一级子进程',os.getpid()) #一级子进程退出
    p = os.fork()
    if p == 0:
        print('二级子进程', os.getpid())#二级子进程S+(等待态)
        f1()
else:
    os.wait() #在父进程中阻塞等待处理子进程退出
    print('父进程', os.getpid())#父进程S+(等待态)
    f2()

