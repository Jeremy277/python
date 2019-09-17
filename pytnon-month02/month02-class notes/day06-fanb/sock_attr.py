'''
    套接字属性
'''

from socket import *

sockfd = socket()

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(('176.234.6.17',5778))
sockfd.listen(3)
confd,data = sockfd.accept()


# print(dir(sockfd))

print('地址类型',socket.family)
print(sockfd.type)
print(sockfd.getsockname())
print(sockfd.fileno())
print(confd.getpeername())

confd.recv(1024)

confd.close()
sockfd.close()

