'''
    thread2
'''
from threading import Thread
from time import sleep

def fun(sec,name):
    print('%s线程开始执行'%name)
    sleep(sec)
    print('%s执行完毕'%name)

jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,)
               ,kwargs={'name':'T%d'%i})
    jobs.append(t)
    t.start()

for i in jobs:  #抢占式执行，谁先执行结束，谁就先回收
    i.join()
