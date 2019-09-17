# http_server.py
#     1. 主要功能 ：
# 【1】 接收客户端（浏览器）请求
# 【2】 解析客户端发送的请求
# 【3】 根据请求组织数据内容
# 【4】 将数据内容形成http响应格式返回给浏览器
#     2. 升级点 ：
# 【1】 采用IO并发，可以满足多个客户端同时发起请求情况
# 【2】 做基本的请求解析，根据具体请求返回具体内容，同时满足客户端简单的非网页请求情况
# 【3】 通过类接口形式进行功能封装

from socket import *
from select import select

class HTTPServer:
    def __init__(self,host='0.0.0.0',port=5299,dir='./'):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host,port)
        #select 监控列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    #1.创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    #2.绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    #3.提供服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print('Listen the port%d'%self.port)
        #设置关注的ID
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c,addr = r.accept()
                    self.rlist.append(c)
                else:
                    #有客户端发请求
                    self.handle(r)
    #4.处理客户端请求
    def handle(self,connfd):
        #接受请求
        request = connfd.recv(4096)
        print(request)
        #客户端断开处理
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return

        #提取请求内容
        request_line = request.splitlines()[0] #切割字节串
        print(request_line)
        info = request_line.decode().split(' ')[1]
        print(info)

        #根据info情况分类 (网页 和 其他）
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd,info)
        else:
            self.get_data(connfd,info)

    def get_html(self,connfd,info):
        if info == '/':
            #主页
            filename = self.dir + '/index.html'
        else:
            #其他网页
            filename = self.dir + info
        try:
            f = open(filename)
        except Exception:
            #没有网页
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry<h1>'
        else:
            #有网页
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += f.read()
        finally:
            connfd.send(response.encode())

    def get_data(self,connfd,info):
        f = open(self.dir + '/gakki.jpg','rb')
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type:image/jpg\r\n'
        response += '\r\n'
        response = response.encode() + f.read()  #字节串
        connfd.send(response)



if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 5277
    DIR = '/home/tarena/python/pytnon-month02/month02-class notes/day12-fanb/static'  #网页目录

    http = HTTPServer(HOST,PORT,DIR)  #实例化对象
    http.serve_forever()  #启动服务
