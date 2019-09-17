'''
    空洞文件
'''
with open('test','wb') as f:
    f.write(b's')
    # f.seek(1024*1024*10)  #向后移动10M
    f.write(b'e')
    print(f.fileno())
