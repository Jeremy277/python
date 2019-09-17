'''
    sem
'''

from  multiprocessing import Process,Semaphore
import time,os

#创建信号量对象
sem = Semaphore(3)

#任务函数
def handle():
    sem.acquire() #执行任务必须消耗一个信号量
    print('开始执行任务：',os.getpid())
    time.sleep(2)
    print('终止任务：', os.getpid())
    sem.release()#增加一个信号量

for i in range(4):  #4个进程
    p = Process(target=handle)
    p.start()
    # p.join()

