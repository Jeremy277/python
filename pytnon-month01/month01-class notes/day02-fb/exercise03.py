#练习
#在控制台 录入商品单价
#在录入数量
#最后获取金额 输入100 计算找零

price = float(input('请输入商品单价：'))
count = float(input('请输入数量：'))
money = float(input('请输入金额：'))
result =str(money - price * count)

print('应找零' + result + '元!')