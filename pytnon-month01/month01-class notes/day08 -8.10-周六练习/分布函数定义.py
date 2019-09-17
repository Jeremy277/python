shang_pin_info = {
101:{'name':'倚天剑','price':10000},
102:{'name':'屠龙刀','price':10000},
103:{'name':'九阳神功','price':10000},
104:{'name':'九阴白骨爪','price':9999},
105:{'name':'乾坤大挪移','price':8888},
106:{'name':'七伤拳','price':7777},
}
#1.定义主页函数
def desktop_fun():
    print('*' * 12,'\n绝招商店\n','*' * 12,'\n按1购买\n',
              '按2结算\n','*' * 12,sep='')

# 2.判断商品是否存在:
def if_exist(num_sp):
    if num_sp in shang_pin_info.keys():
        if num_sp not in shopping_cart.keys():
            shopping_cart[num_sp] = shang_pin_info[num_sp]
            shopping_cart[num_sp]['number'] = 1
            print('添加到购物车!')
        elif num_sp in shopping_cart.keys():
            shopping_cart[num_sp]['number'] += 1
            print('添加到购物车!')
    else:
        print('商品不存在!')
# 3.显示购物车函数
def show_allsh():
    print('*' * 12, '\n购物车:')
    print('编号  名称  价格 数量')
    for kc, vc in shopping_cart.items():
        print(kc, end=' ')
        for vc2 in vc.values():
            print(vc2, end=' ')
        print()
    print('*' * 12)
#4.结算函数:
def account():
    money = int(input('请输入金额:'))
    pay_money = 0

    for k_pay in shopping_cart:
        pay_money += shopping_cart[k_pay]['price'] * shopping_cart[k_pay]['number']
    if money < pay_money:
        print('金额不足!')
    else:
        result = money - pay_money
        print('\n购买成功,支付%d金元宝,消费%d金元宝,找零%d金元宝\n' % (money,pay_money,result))
#5.主程序
def main():
    global shopping_cart
    shopping_cart = {}
    desktop_fun()
    while True:
        choice = int(input('请输入选项:\n'))
        print('编号 名称  价格 ')
        if choice == 2:
            print('购买完成,准备结算\n')
            break
        if choice == 1:
            for k, v in shang_pin_info.items():
                print(k, end=' ')
                for v1 in v.values():
                    print(v1, end=' ')
                print()
            print('*' * 12)
            num_sp = int(input('请输入商品编码:\n'))
            if_exist(num_sp)
            desktop_fun()
    show_allsh()
    account()
#启动程序
main()
input('按回车键退出!')


