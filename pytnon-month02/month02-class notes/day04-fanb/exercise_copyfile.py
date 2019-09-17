#拷贝文件
f = open('test','r')
c = open('copyfile', 'w')
c.write(f.read())
f.close()
c = open('copyfile','r')
print(c.read(2))