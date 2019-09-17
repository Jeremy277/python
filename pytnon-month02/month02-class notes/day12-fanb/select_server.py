#IO多路复用
import select
from socket import *

#创建套接字作为关注IO对象
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',5299))
s.listen(3)

#设置关注列表
rlist = [s]
wlist = []
xlist = []

#循环连接服务端
while True:
    rs,ws,xs = select.select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print('connect from',addr)
            rlist.append(c)

        else:
            data = r.recv(1024).decode()
            if not data:
                # break   #跳出循环
                rlist.remove(r)
                r.close()
                continue
            print(data)
            r.send(b'OK')