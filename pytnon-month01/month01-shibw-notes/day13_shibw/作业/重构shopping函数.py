#重构shopping:
#商品模型  id name price
#订单模型   cid count

#购物车控制台界面视图
#入口 显示界面 1 2 q
#选择 1 2 q
#1 执行的函数
#2 执行的函数

#购物车逻辑控制器
#加载商品
#添加到订单
#生成订单
#计算总价



#-----------
class Shopping_info:
    def __init__(self,name,price,num=0):
        self.num = num
        self.name = name
        self.price = price

class Cart_info:
    def __init__(self,cnum,count):
        self.cnum = cnum
        self.count = count

class ShoppingManagerController:

    __info_num = 100
    def __init__(self):
        self.shang_pin_info = []
        self.cart_info = []
    #1.添加商品信息
    def add_info(self,info):
        info.num = self.__generate_num()
        self.shang_pin_info.append(info)
    #生成id
    def __generate_num(self):
        ShoppingManagerController.__info_num += 1
        return ShoppingManagerController.__info_num
    #2.打印商品信息
    def print_info(self):
        print('*' * 50)
        for item in self.shang_pin_info:
            print(item.num,item.name,item.price)
        print('*' * 50)
    #检查商品id
    def __check_id(self,sp_num):
        for item in self.shang_pin_info:
            if item.num == sp_num:
                return True
    #3.添加购物车
    def add_cart(self,info):
        if self.__check_id(info.cnum):
            self.cart_info.append(info)
            return True
    #4.打印购物车
    def print_cart_info_total_price(self):
        total_price = 0
        print('*' * 50)
        for item in self.cart_info:
            for item_s in self.shang_pin_info:
                if item.cnum == item_s.num:
                    print(item.cnum,item.count,item_s.price)
                    total_price += item.count * item_s.price
        print('*' * 50)
        return total_price

    #5.结算
    def paying(self,money):
        total_price = self.print_cart_info_total_price()
        if money >= total_price:
            change = money - total_price
            return change

class ShoppingManagerView:
    #1.生成视图界面中的管理器
    def __init__(self):
        self.__manger = ShoppingManagerController()
    #2.显示界面
    def __display_menu(self):
        print('''
******************
    夺命商店1.0
******************
    按1购买
    按2结算
    按q退出
******************
''')
    #3. 主程序:界面入口
    def main(self):
        self.__display_menu()
        self.__input_info()
        choice = None
        while choice != 'q':
            choice = input('请输入选项:')
            if choice == 'q':
                print('谢谢使用,退出商店!')
                break
            elif choice == '1':
                self.__output_info()
                self.__add_cart()
            elif choice == '2':
                self.__output_cart_info()
                self.__paying()
            else:
                print('请输入正确选项!')
    #4.加载商品信息
    def __input_info(self):
        s01 = Shopping_info( '倚天剑', 10000)
        s02 = Shopping_info( '屠龙刀', 9000)
        s03 = Shopping_info( '七伤拳', 8000)
        s04 = Shopping_info( '一阳指', 7000)
        s05 = Shopping_info( '断肠剑', 7000)
        self.__manger.add_info(s01)
        self.__manger.add_info(s02)
        self.__manger.add_info(s03)
        self.__manger.add_info(s04)
        self.__manger.add_info(s05)
    #5.显示商品信息
    def __output_info(self):
        print('商品信息:')
        self.__manger.print_info()
    #6.添加购物车
    def __add_cart(self):
        cnum = int(input('\n请输入需要购买的商品编号:'))
        count = int(input('请输入购买的商品数量:'))
        cart_info = Cart_info(cnum,count)
        if self.__manger.add_cart(cart_info):
            print('\n添加购物车成功!')
        else:
            print('\n添加购物车失败!')

    #7.打印购物车信息并计算总价:
    def __output_cart_info(self):
        print('\n购物车商品信息:')
        res = self.__manger.print_cart_info_total_price()
        print('\n共计%s金元宝.' % res)
    #8.结算
    def __paying(self):
        money = int(input('\n请支付金元宝:'))
        change = self.__manger.paying(money)
        if change:
            print('\n支付%s金元宝,购买成功，找零%.2f金元宝' % (money,change))
            print('购买成功!')
        else:
            print('\n购买失败!')

view = ShoppingManagerView()
view.main()









# #测试显示功能
# #生成对象
# s01 = Shopping_info(101,'倚天剑',10000)
# s02 = Shopping_info(102,'屠龙刀',9000)
# s03 = Shopping_info(103,'七伤拳',8000)
# s04 = Shopping_info(104,'一阳指',7000)
# #生成管理器对象
# manger = ShoppingManagerController()
# #添加商品信息
# manger.add_info(s01)
# manger.add_info(s02)
# manger.add_info(s03)
# manger.add_info(s04)
# #打印商品信息
# manger.print_info()
# # #测试添加购物车
# c01 = Cart_info(101,2)
# c02 = Cart_info(106,2)
# print(bool(manger.add_cart(c01)))
# print(bool(manger.add_cart(c02)))
# # manger.add_cart(c02)
#
# # #打印购物车
# manger.print_cart_info_total_price()
# # #测试结算功能
# manger.paying(37000)
# #
