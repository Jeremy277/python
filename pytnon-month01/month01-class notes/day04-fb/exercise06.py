#在控制台输入字符串，打印编码值
# str_1 = input('输入字符串：')
# for i in str_1:
#     print('字符：%s 编码：%d'% (i,ord(i)))




#录入编码值，打印字符，若录入空字符串 退出程序
while True:
    str_2 = input('输入编码值：')
    if str_2 == '':
        print('输入空字符，退出')
        break
    else:
        str_2 = int(str_2)
        print('编码：%d 字符：%s' % (str_2, chr(str_2)))