from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

p = Process(target=worker,args=(2,'Jer'))
# p = Process(name = '进程',target=worker,kwargs={'name':'Jer','sec':2})
p.daemon = True
# print('name:',p.name)
# print('pid:',p.pid)
# print('is alive:',p.is_alive())

p.start()
sleep(3)
print('ziname:',p.name)
print('zipid:',p.pid)
print('zi is alive:',p.is_alive())
# p.join()