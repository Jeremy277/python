'''
    发送文件
    思路：循环读取文件 发送
'''

from socket import *

s = socket()
s.connect(('127.0.0.1',8888))

f = open('quanshui.jpg','rb')

while True:
    #边读 边发
    data = f.read(1024)
    if not data:#文件结尾
        break
    s.send(data)


f.close()
s.close()