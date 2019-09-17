##普通客户端——循环收发——tcp

from socket import *

sockfd = socket()
sockfd.connect(('127.0.0.1',5277))

while True:
    msg = input('msg>>')
    if not msg:
        break
    sockfd.send(msg.encode())
    data = sockfd.recv(1024)
    print('from server:',data.decode())
sockfd.close()



