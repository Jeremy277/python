
#非阻塞 io 演示

from socket import *
from time import ctime,sleep

f = open('log.txt','a')

s = socket()
s.bind(('0.0.0.0',5278))
s.listen(5)

#设置非阻塞
# s.setblocking(False)

s.settimeout(3)

while True:
    try:
        c,addr = s.accept()
        print('Connect from ',addr)
    except BlockingIOError as e:
        sleep(2)
        f.write(ctime()+':'+ str(e) + '\n')
    else:
        c.send(b'ok')
        data = c.recv(1024)
        print(data.decode())
