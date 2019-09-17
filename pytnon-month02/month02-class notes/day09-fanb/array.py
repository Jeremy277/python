'''
array
'''

from multiprocessing import Process,Array
import time,random

#创建共享内存，初始[1,2,3,4,5]
# shm = Array('i',[1,2,3,4,5])
# shm = Array('i',4) #创建共享内存，初始[0,0,0,0]
shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i,end=' ')
    shm[0] = b'H'

p = Process(target=fun)
p.start()
p.join()
print()
# for i in shm:
#     print(i,end=' ')
#只能用于打印共享内存字节串
print(shm.value) #b'Hello'

