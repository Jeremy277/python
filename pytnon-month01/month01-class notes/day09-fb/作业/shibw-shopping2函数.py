shang_pin_info = {
101:{'name':'倚天剑','price':10000},
102:{'name':'屠龙刀','price':10000},
103:{'name':'九阳神功','price':10000},
104:{'name':'九阴白骨爪','price':9999},
105:{'name':'乾坤大挪移','price':8888},
106:{'name':'七伤拳','price':7777},
}
#定义购物车清单
cart_info = []

prompt = '''************
商店
************
按1购买
按2结算
按q退出
************
'''
#菜单:
#提示字符串让用户输入1/2/q
#如果1
#购物功能
#如果2
#结算功能
#如果q
def select_menu():
    while True:
        item = input(prompt)
        if item == 'q':
            break
        elif item == '1':
            buying()
        else:
            select_menu()
#购物功能:
def buying():
    print_info()
    creat_order()
    print('添加购物车成功!')
#显示商品
def print_info():
    print('*' * 50)
    for key, value in shang_pin_info.items():
        print('%d     %s     %d' % (key, value['name'], value['price']))
    print('*' * 50)
#检测商品是否存在
def check_id():
    while True:
        cid = int(input('请输入商品编号：'))
        if cid in shang_pin_info:
            break
        else:
            print('商品不存在，请重新输入！')
    return cid
#添加到购物车清单
def creat_order():
    #需要合法的商品编号,有check-id提供
    cid = check_id()
    count = int(input('请输入商品数量：'))
        # 如果商品编号正确　加购物车
    cart_info.append({'cid': cid, 'count': count})

#结算功能:
def settlment():
    print_order()
    total_price = calc_total_price()
    paying(total_price)
#打印购物清单
def print_order():
    print(cart_info)
    print('*' * 50)
    print('购物车')
    print('*' * 50)
    # 购物清单价格　＝　数量　＊　商品单价
    # 商品单价需要用过cid去shang_pin_info查找
    for item in cart_info:
        price = shang_pin_info[item['cid']]['price']  # 记住随时随地都可以灵活的从字典里取数据
        print('%d     %d      %d' % (item['cid'], item['count'], item['count'] * price))
        print('*' * 50)
#计算总价格
def calc_total_price():
    zong_jia = 0
    for order in cart_info:
        price = shang_pin_info[order['cid']]['price']
        zong_jia += order['count'] * price
    return zong_jia

#接受用户输入 完成支付
def paying(zong_jia):
    while True:
        money = float(input('总价为%d元，请输入金额：' % zong_jia))
        # 如果money>=zongjia 找零
        # 如果money<zongjia 重新输入
        if money >= zong_jia:
            print('购买成功，找零%.2f' % (money - zong_jia))
            # 清空购物车清单
            cart_info.clear()
            break
        else:
            print('金额不足，请重新输入')


select_menu()









