# 2.在控制台获取年龄
# 如果小于0 打印输入错误
# 如果 小于2  打印是婴儿
# 如果 小于2~13  儿童
#        13~20  青年
#        20~65  成年人
#        65~130 老年人
#        超过130 不可能

age = int(input('请输入年龄：'))
#简化比较逻辑，前述以判断的，无需再判断
if age < 0:
    print('输入错误！')
elif age < 2:
    print('婴儿')
elif age < 13:
    print('儿童')
elif age < 20:
    print('青年')
elif age < 65:
    print('老年')
elif age < 130:
    print('婴儿')
else:
    print('妖怪')
