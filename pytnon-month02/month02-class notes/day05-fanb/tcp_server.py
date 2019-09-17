#tcp套接字服务端流程

# 注意：流程  功能性代码

import socket

#创建流式套接字对象
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',9978))
#设置监听
sockfd.listen(5)
#等待处理客户端连接请求
print('Waitting for connect...')
connfd,addr = sockfd.accept()
print('Connect from',addr)
#消息收发 #二进制
data = connfd.recv(5)
print('Receive:',data.decode())
n = connfd.send(b'Thanks')
print('Send %d bytes' % n)


# #关闭套接字
connfd.close()
sockfd.close()

