#重构shopping:
#商品模型  id name price
#订单模型   cid count
#       为满足删除 修改订单 再加一个数据commodity
# class ShoppingManagerController:
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
class Shopping_info_Model:
    def __init__(self,id,name,price,):
        self.id = id
        self.name = name
        self.price = price

class Cart_info_Model:
    def __init__(self,cid,count):
        self.cid = cid
        self.count = count

class ShoppingManagerController:
    def __init__(self):
        self.__shopping_list = self.__load_shopping_info()
        self.__cart_list = []
    @property
    def shopping_list(self):
        return self.__shopping_list
    @property
    def cart_list(self):
        return self.__cart_list
    #加载商品信息
    def __load_shopping_info(self):
        return [
            Shopping_info_Model(101,'倚天剑',10000),
            Shopping_info_Model(102,'屠龙刀',10000),
            Shopping_info_Model(103,'九阳神功',10000),
            Shopping_info_Model(104,'九阴白骨爪',9999),
            Shopping_info_Model(105,'乾坤大挪移',8888),
            Shopping_info_Model(106,'七伤拳',7777),
        ]
    def add_cart(self,info):
        self.cart_list.append(info)
    def total_price(self):
        total_price = 0
        for item_c in self.cart_list:
            for item_s in self.shopping_list:
                if item_c.cid == item_s.id:
                    print(item_c.cid,item_c.count,item_s.price)
                    total_price += item_c.count * item_s.price
        return total_price
    def check_id(self,cid):
        for item in self.shopping_list:
            if cid == item.id:
                return True
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
        choice = None
        while choice != 'q':
            choice = input('请输入选项:')
            if choice == 'q':
                print('谢谢使用,退出商店!')
                break
            elif choice == '1':
                self.__input_shopping_info()
                self.__add_cart()
            elif choice == '2':
                self.__input_cart_total_price()
                self.__paying()
            else:
                print('请输入正确选项!')
    def __input_shopping_info(self):
        for item in self.__manger.shopping_list:
            print(item.id,item.name,item.price)
    def __add_cart(self):
        cid = int(input('请输入要购买的商品编号：'))
        if self.__manger.check_id(cid):
            count = int(input('请输入购买数量：'))
            cart_info = Cart_info_Model(cid,count)
            self.__manger.add_cart(cart_info)
        else:
            print('商品编号不存在')
    def __input_cart_total_price(self):
        total_money = self.__manger.total_price()
        print('总计',total_money)
        return total_money
    def __paying(self):
        money = int(input('请输入金额：'))
        if money >= self.__input_cart_total_price():
            print('购买成功，找零',money - self.__input_cart_total_price())
            self.__manger.cart_list.clear()
        else:
            print('金额不足')

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
