"""
    群聊天客户端
"""
from socket import *
import os,sys

#服务器地址
ADDR = ('127.0.0.1',5277)

#发送消息
def send_msg(s,name):
    while True:
        try:
            text = input('>>')
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = 'Q'+ name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出群聊天')
        msg = 'C %s %s'%(name,text)
        s.sendto(msg.encode(),ADDR)
#接受消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(4096)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+ '\n>>',end='')

#搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    #进入聊天室
    while True:
        name = input('请输入昵称：')
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        #接受反馈
        data,addr = s.recvfrom(128)
        if data == b"OK":
            print('您已进入聊天室！')
            break
        else:
            print(data.decode())

    #已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit('Error!')
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)


if __name__ == '__main__':
    main()

