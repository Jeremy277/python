'''
    multiprocessing模块创建进程
'''

import multiprocessing as mp
from time import sleep

a = 1
#进程函数
def fun():
    print('开始子进程')
    sleep(3)
    global a
    print('a:',a)
    a = 10000
    print('子进程结束')

#创建进程对象
p = mp.Process(target=fun)
p.start()#启动进程
sleep(2)
print('父进程')
p.join()#回收进程   阻塞

print('==============')
print('a:',a)
