'''
    udp_client
'''
from socket import *
import struct

#1.创建udp套接字
#服务器地址
ADDR = ('127.0.0.1',5277)
sockfd = socket(AF_INET,SOCK_DGRAM)

#2.循环收发消息
while True:
    id = int(input('学号:'))
    name = input('姓名:')
    age = int(input('年龄:'))
    score = int(input('分数:'))
    # if not id or age or name or score:
    #     print('udp_client exit')
    #     break
    st = struct.Struct('i2sii')
    stu = st.pack(id,name.encode(),age,score)
    n = sockfd.sendto(stu,ADDR)

#3.关闭套接字
sockfd.close()