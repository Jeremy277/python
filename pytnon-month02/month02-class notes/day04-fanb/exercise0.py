#刷新缓冲区

f = open ('test','w')
# f = open ('test','w',1)#行缓冲

while True:
    data = input('>>')
    if not data:
        break
    f.write(data + '\n')
    # f.flush()

f.close()