'''
    udp_server
'''
from socket import *

#1.创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#2.绑定地址
server_addr = ('0.0.0.0',5277)
sockfd.bind(server_addr)

#3.循环收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    print('Msg from %s:%s' % (addr,data.decode()))
    data_s = input('Send:')
    n = sockfd.sendto(b'Thanks',addr)
    print('Send %d bytes' % n)


#4.关闭套接字
sockfd.close()