from project.shopping_system.bll import ShoppingManagerController
from project.shopping_system.model import Shopping_info, Cart_info


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
        self.__manger.add_info(Shopping_info( '倚天剑', 10000))
        self.__manger.add_info(Shopping_info( '屠龙刀', 9000))
        self.__manger.add_info(Shopping_info( '七伤拳', 8000))
        self.__manger.add_info(Shopping_info( '一阳指', 7000))
        self.__manger.add_info(Shopping_info( '断肠剑', 7000))
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
        if change >= 0:
            print('\n支付%s金元宝,购买成功，找零%.2f金元宝' % (money,change))
            print('购买成功!')
            self.__manger.cart_info.clear()
        else:
            print('\n购买失败!')