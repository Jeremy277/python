'''
    结束一个文件
'''

from socket import *

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

c,addr = s.accept()
print('Connect from',addr)

#打开文件
f = open('backup_qs.jpg','wb')
#循环接受内容 ，写入文件
while True:
    #边收 边写
    data = c.recv(5)
    #若为空 以为客户端退出
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()