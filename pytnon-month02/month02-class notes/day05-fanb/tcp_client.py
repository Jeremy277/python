#tcp套接字客户端流程

# 注意：流程  功能性代码

from socket import *

#创建流式套接字对象
sockfd = socket()
#地址
sockfd.connect(('176.234.6.17',9978))#服务器地址

#消息先发后收 #二进制
msg = input('Msg:')
sockfd.send(msg.encode())
data = sockfd.recv(1024)
print('From srever:',data.decode())

# #关闭套接字
sockfd.close()