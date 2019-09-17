"""
测试用例
"""
from multiprocessing import  Process
from threading import Thread
import time
# 计算
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# io
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()
#单进程
# start = time.time()
# for i in range(10):
#     # count(1,1)
#     io()
# print('执行时间',time.time()-start)
#执行时间 7.188409090042114
#执行时间 5.065692663192749

#10进程
start = time.time()
jobs = []
for i in range(10):
    # p_c = Process(target=count,args=(1,1))
    p_io = Process(target=io)
    # jobs.append(p_c)
    jobs.append(p_io)
    # p_c.start()
    p_io.start()

for i in jobs:
    i.join()
end = time.time()
print('执行时间',end-start)
#执行时间 3.3569705486297607
#执行时间 1.976289987564087

#10线程
# start = time.time()
# jobs = []
# for i in range(10):
#     # p_c = Thread(target=count,args=(1,1))
#     p_io = Thread(target=io)
#     # jobs.append(p_c)
#     jobs.append(p_io)
#     # p_c.start()
#     p_io.start()
#
# for i in jobs:
#     i.join()
# end = time.time()
# print('执行时间',end-start)
#执行时间 7.455246448516846
# 执行时间 4.696223020553589