#短路逻辑

# result = 1 == 1 and  input('请输入a:') == 'a'
#
# print(result)
# a = (1 + 1
#      + 2 + 1
#      +1 + 4)
# a = 1 + 1 + 2 \
#     + 5 + 9 + 8

# 练习
#当钱不够时提示金额不足，钱够时 提示找零

price = float(input('请输入商品单价：'))
count = float(input('请输入数量：'))
money = float(input('请输入金额:'))
result = money - price * count

if result < 0:
    print('您的余额不足！')
else:
    print('购买成功，找零为' + str(result) + '元！')
