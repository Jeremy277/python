'''
    fork进程
'''

import os
from time import sleep

print('===============')
a = 1
pid = os.fork()

if pid < 0:
    print('创建进程失败')
elif pid == 0:
    sleep(30)
    print('子进程')
    print(a)
    a = 100
else:
    sleep(1)
    print('父进程')
    print(a)

print('测试',a)