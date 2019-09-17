#文件写操作
f = open('test','w')
# f = open('test','wb')
# f = open('test','ab')

#写操作
f.write(b'hello,jer.\n')
f.write('你好,西西\n'.encode())
# f.close()

#写入列表内容：
l = ['hello\n','hahaha\n']
f.writelines(l)

# print('a b c d'.split())