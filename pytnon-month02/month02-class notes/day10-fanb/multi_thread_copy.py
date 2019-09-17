'''
    多线程同步互斥下载视频
'''
import os
from threading import Thread, Lock
from time import sleep

lock = Lock()
urls = [
    '/home/tarena/视频/',
    '/home/tarena/图片/',
    '/home/tarena/文档/',
    '/home/tarena/下载/',
    '/home/tarena/音乐/',
    '/home/tarena/桌面/',
    '/home/tarena/模板/',
    '/home/tarena/示例/'
]
filename = input('要下载的文件：')
explorer = []
for i in urls:
    if os.path.exists(i+filename):
        explorer.append(i+filename)

num = len(explorer)
if num == 0:
    print('没有找到资源')
    os._exit(0)
size = os.path.getsize(explorer[0])
block_size = size // num + 1
print(explorer)
print(size)

#共享资源
fd = open(filename,'wb')

#下载文件
def load(path,num):
    f = open(path,'rb')
    seek_types = block_size*num
    f.seek(seek_types)
    size = block_size

    lock.acquire()
    fd.seek(block_size*num)
    while True:
        if size < 1024:
            data = f.read(size)
            fd.write(data)
            break
        else:
            data = f.read(1024)
            fd.write(data)
            size -= 1024
    lock.release()


#分配线程
n = 0
jobs = []
for path in explorer:
    t = Thread(target=load,args=(path,n))
    jobs.append(t)
    t.start()
    n += 1
    print('线程%d下载完成！'% n)
for i in jobs:
    i.join()

print('%s下载完成！' % filename)