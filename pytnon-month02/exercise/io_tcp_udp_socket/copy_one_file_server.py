#上传文件 服务端

from socket import *

s = socket()
s.bind(('0.0.0.0',5277))
s.listen(2)

c,addr = s.accept()
print('Connect from',addr)
f = open('copy_ship.bmp','wb')
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
f.close()
s.close()
c.close()