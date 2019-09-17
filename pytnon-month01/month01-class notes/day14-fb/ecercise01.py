#定义一个图形管理器类
#1.保存所有图形
#2.提供计算 所有图形总面积的功能
#封装
#------------------------------------------
class GraphManagerController:
    def __init__(self):
        self.__graph_list = []

    @property
    def graph_list(self):
        return self.__graph_list

    def add_graph(self,graph):
        if not isinstance(graph, Graphic):
            raise ValueError('目标对图形免疫')
        self.__graph_list.append(graph)

    def calc_total_area(self):
        total_area = 0
        for item in self.graph_list:
            total_area += item.calc_area()
        return total_area
#继承
#----------------------------------------
class Graphic:
    def calc_area(self):
        raise NotImplementedError('如果子类不重写则异常')
#多态
#-----------------------------------------
class Round(Graphic):
    def __init__(self,radius):
        self.radius = radius
    def __str__(self):
        return '圆形'

    def calc_area(self,):
        return 3.14*self.radius**2

class Rectangle(Graphic):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def __str__(self):
        return '矩形'

    def calc_area(self):
        return self.length*self.width

    # def print_graph(self):
    #     for item in self.__graph_list:
    #         print(item)




#测试代码:
c01 = Round(5)
r01 = Rectangle(10,20)
manger = GraphManagerController()
manger.add_graph(c01)
manger.add_graph(r01)
for item in manger.graph_list:
    print(item)
print(manger.graph_list)
print(manger.calc_total_area())





