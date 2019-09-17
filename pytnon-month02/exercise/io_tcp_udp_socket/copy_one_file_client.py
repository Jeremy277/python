#上传文件 客户端

from socket import *

s = socket()
s.connect(('127.0.0.1',5277))

f = open('ship.bmp','rb')
while True:
    data = f.read(1024)
    if not data:
        print('上传成功')
        break
    s.send(data)
f.close()
s.close()
