# 聊天室-服务端
from socket import *

#定义全局变量
HOST = '0.0.0.0'
PORT = 5299
ADDR = (HOST,PORT)
user = {}
#1.搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    do_request(s)

#2.处理请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            do_chat(s, tmp[1], tmp[2])
        # elif tmp[0] == 'Q':
        #     do_quit(s, tmp[1]

#3.具体处理请求操作
def do_login(s,name,addr):
    if name in user:
        s.sendto('昵称已存在'.encode(),addr)
        return #必须
    else:
        s.sendto(b'OK',addr)
    msg = '欢迎%s加入聊天室'% name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr

# 处理聊天
def do_chat(s,name,text):
    msg = "\n%s : %s"%(name,text)
    for i in user:
        # 不发送自己
        if i != name:
            s.sendto(msg.encode(),user[i])


if __name__ == '__main__':
    main()