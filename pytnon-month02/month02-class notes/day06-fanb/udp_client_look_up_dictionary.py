'''
    网络字典_客户端
'''
from socket import *

#1.创建udp套接字
#服务器地址
ADDR = ('127.0.0.1',5277)
sockfd = socket(AF_INET,SOCK_DGRAM)

#2.循环收发消息
while True:
    data = input('Msg:')
    if not data:
        print('udp_client exit')
        break
    n = sockfd.sendto(data.encode(),ADDR)
    print('Send %d bytes' % n)
    msg,addr = sockfd.recvfrom(1024)
    print('From server:',msg.decode())

#3.关闭套接字
sockfd.close()