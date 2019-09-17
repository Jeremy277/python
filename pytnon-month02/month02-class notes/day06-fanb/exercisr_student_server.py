'''
    udp_server
'''
from socket import *
import struct

#1.创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#2.绑定地址
server_addr = ('0.0.0.0',5277)
sockfd.bind(server_addr)

#3.循环收发消息
f = open('stu_info.txt','a')
st = struct.Struct('i2sii')
while True:
    data,addr = sockfd.recvfrom(1024)
    stu = st.unpack(data)
    print('Msg from %s:%s' % (addr,stu))
    # for item in stu:
    #     f.write(item)
    info = '%d %-10s %d %d\n'%stu
    f.write(info)
    f.flush()




#4.关闭套接字
f.close()
sockfd.close()