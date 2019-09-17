'''
    网络字典_服务端
'''
from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

server_addr = ('0.0.0.0',5277)
sockfd.bind(server_addr)

print("Waiting for connect...")

while True:
    f = open('dict.txt')
    data,addr = sockfd.recvfrom(1024)
    word = data.decode()
    print('Msg from %s:%s' % (addr, word))
    for line in f:
        w = line.split(' ')[0]
        # 遍历的单词已经大于目标,说明找不到了
        if w > word:
            n = sockfd.sendto('没有找到该单词'.encode(), addr)
            print('Send %d bytes' % n)
            break

        elif w == word:
            n = sockfd.sendto(line.encode(), addr)
            print('Send %d bytes' % n)
            break

    else:
        n = sockfd.sendto('没有找到该单词'.encode(), addr)
        print('Send %d bytes' % n)
        print("没有找到该单词")
        break
    f.close()









