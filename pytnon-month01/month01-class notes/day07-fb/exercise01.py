#
set_1 = set()
while True:

    str_1 = input('输入字符:')
    if str_1 == '':
        print('退出')
        break
    set_1.add(str_1)
for i in set_1:
    print(i)
