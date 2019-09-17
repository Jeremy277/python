'''
    thread2
'''
from threading import Thread
from time import sleep

def fun(sec,name):
    print('%s线程开始执行'%name)
    sleep(sec)
    print('%s线程执行完毕'%name)



t = Thread(name='小县城' ,target=fun,args=(2,1))
# print(t.setDaemon(True))
t.start()
t.setName('xiaoxiancheng')
print(t.getName())

print(t.isDaemon())
print(t.is_alive())
t.join()
print(t.is_alive())
# t.join()
