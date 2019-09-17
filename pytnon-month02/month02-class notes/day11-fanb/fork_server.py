'''
    基于fork的多进程并发模型
'''
from socket import *
import os
import signal

#全局变量
HOST = '0.0.0.0'
PORT = 5299
ADDR = (HOST,PORT)

#客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

#创建套接字
s =socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#创建信号处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print('Listen the port 5277...')
# n = 0
while True:
    #等待客户端循环连接
    try:
        c,addr = s.accept()
        print('Connect from',addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    # n += 1
    # print(n)

    # 创建进程
    pid = os.fork()
    # if pid < 0:   #可以不写，因为如果创建失败，继续循环
    #     pass
    if pid == 0:
        s.close()    #防止执行循环部分
        handle(c)   #和客户端交互
        os._exit(0)  #客户端结束后，子进程结束
    else:
        c.close()

