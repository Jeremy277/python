#tcp 客户端

from socket import *

st = socket()

st.connect(('127.0.0.1',5277))

msg = input('输入：')
st.send(msg.encode())
print('发送成功')
print(st.recv(1024).decode())

st.close()

