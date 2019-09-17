#输入商品信息,打印:
dic_1 = {}
while True:
    sale_w = input('输入商品名称:')
    if sale_w == '':
        print('退出')
        break
    price = int(input('输入商品单价:'))
    dic_1[sale_w] = price

for key,value in dic_1.items():
    print('%s的单价为%.1f' % (key,value))
if '游戏机' in dic_1:
    print('游戏机的单价%.1f' % dic_1['游戏机'])



