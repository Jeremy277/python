# 1. process完成，使用两个子进程同时
# 复制一个文件，一个进程复制上半部分，另一个复制下半部分，
# 分别复制到一个新的文件里。

from multiprocessing import Process
from time import sleep
import os

f = open('test.txt','r')
data_list = f.readlines()
print(data_list)#文本内容中本来就有换行
n = len(data_list)
f.seek(0)

def copy_up():
    f = open('copy_up.txt','w')
    f.writelines(data_list[0:n//2])

def copy_down():
    f = open('copy_down.txt','w')
    f.writelines(data_list[n//2:])

things = [copy_up,copy_down]
jobs = []
for copy in things:
    p = Process(target = copy)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
