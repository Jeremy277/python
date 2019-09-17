class ShoppingManagerController:

    __info_num = 100
    def __init__(self):
        self.__shang_pin_info = []
        self.__cart_info = []

    @property
    def shang_pin_info(self):
        return self.__shang_pin_info
    @property
    def cart_info(self):
        return self.__cart_info

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
            return money - total_price
