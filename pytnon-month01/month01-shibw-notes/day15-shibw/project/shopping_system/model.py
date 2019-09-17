class Shopping_info:
    def __init__(self,name,price,num=0):
        self.num = num
        self.name = name
        self.price = price

class Cart_info:
    def __init__(self,cnum,count):
        self.cnum = cnum
        self.count = count