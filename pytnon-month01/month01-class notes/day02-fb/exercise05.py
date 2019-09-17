#练习05
#古代称一斤16两 33两 2斤1两
# 在控制台获取两
# 输出几斤几两

liang_ = int(input('\33[33m请输入两：\33[0m'))

jin = liang_ // 16
liang = liang_ % 16

print('\33[31m%d斤%d两\33[0m。' % (jin,liang))