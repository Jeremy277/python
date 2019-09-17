# 1. process完成，使用两个子进程同时
# 复制一个文件，一个进程复制上半部分，另一个复制下半部分，
# 分别复制到一个新的文件里。

from multiprocessing import Process
import os

size = os.path.getsize('qs.jpg')
f = open('qs.jpg','rb')

def copy_top():
    ft = open('qs_top.jpg','wb')
    ft.write(f.read(size//2))
    ft.close()

def copy_bot():
    ft = open('qs_bot.jpg','wb')
    f.seek(size//2)
    ft.write(f.read())
    ft.close()

p1 = Process(target=copy_top)
p2 = Process(target=copy_bot)
p1.start()
p2.start()
p1.join()
p2.join()

