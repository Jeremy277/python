#tcp 服务端

from socket import *

st = socket()

st.bind(('127.0.0.1',5277))

st.listen(3)

print('等待连接：')
ct,addr = st.accept()
print('与',addr,'连接')

data = ct.recv(1024)
print('接收：',data.decode())
ct.send('服务器已收到'.encode())

ct.close()
st.close()

