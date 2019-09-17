'''
    queue
'''

from multiprocessing import Queue,Process
from time import sleep
from random import randint

#创建消息队列
q = Queue(5)

#请求进程
def request():
    for i in range(10):
        sleep(0.5)
        t = (randint(1,100),randint(1,100))
        q.put(t)
        print('====================')
        print('队列是否为满:',q.full())
        print('获取队列消息个数：',q.qsize())


#数据处理进程
def handle():
    while True:
        sleep(2)
        x,y = q.get()
        print('数据处理结果x+y:',x+y)
        print('队列是否为满:',q.full())
        print('获取队列消息个数：', q.qsize())

#创建进程
p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p1.join()