'''
    value
'''
from multiprocessing import Value,Process
from time import sleep
from random import randint

#创建共享内存
money = Value('i',5000)

#操作内存
def man():
    for i in range(30):
        sleep(0.2)
        money.value += randint(1,1000)

def girl():
    for i in range(30):
        sleep(0.15)
        money.value -= randint(100,800)

#创建进程
p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p1.join()
print('月攒:',money.value)