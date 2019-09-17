with open('test','wb+') as f:
    f.write(b'hello,world')
    # f.write('早安，最好的我们'.encode())
    print('文件偏移量：',f.tell())#1个汉字：偏移3个字节
    f.seek(9)
    print(f.read())

