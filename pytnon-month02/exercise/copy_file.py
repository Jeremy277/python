#copy file

filename = input('文件名：')

fr = open(filename,'rb')
fw = open('copy-'+filename,'wb')

while True:
    data = fr.read(1024)
    if not data:
        print('copy over')
        break
    fw.write(data)

fr.close()
fw.close()