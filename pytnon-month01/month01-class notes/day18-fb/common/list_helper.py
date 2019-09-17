"""
    定义项目中所有对容器的操作。
"""

class ListHelper:
    """
        列表助手类
    """
    @staticmethod
    def find_all(iterable_target,func_condition):
        """
            在可迭代对象中，查找满足条件的所有元素。
        :param iterable_target:可迭代对象
        :param func_condition:所有条件
        :return:生成器对象
        """
        for item in iterable_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable_target, func_condition):
        """
            在可迭代对象中，查找满足条件的单个元素。
        :param iterable_target:可迭代对象
        :param func_condition:所有条件
        :return:生成器对象
        """
        for item in iterable_target:
            if func_condition(item):
                return item

    @staticmethod
    def sum_data(iterable_target,func_condition):
        """
                    在可迭代对象中，计算所有参数之和。
                :param iterable_target:可迭代对象
                :param func_condition:所有条件
                :return:生成器对象
                """
        sum_data = 0
        for item in iterable_target:
            sum_data += func_condition(item)
        return sum_data

    @staticmethod
    def get_data(iterable_target, func_condition):
        """
                    在可迭代对象中，获取名称和技能。
                :param iterable_target:可迭代对象
                :param func_condition:所有条件
                :return:生成器对象
                """
        for item in iterable_target:
            yield func_condition(item)

    @staticmethod
    def max_data(iterable_target, func_condition):
        """
                    在可迭代对象中，获取最大数据的技能。
                :param iterable_target:可迭代对象
                :param func_condition:所有条件
                :return:生成器对象
                """
        max_data = iterable_target[0]
        for i in range(1,len(iterable_target)):
            # if max_data.atk < iterable_target[i].atk:
            if func_condition(max_data) <\
                    func_condition(iterable_target[i]):
                max_data = iterable_target[i]
        return max_data

    @staticmethod
    def sort_data(iterable_target, func_condition):
        """
                    在可迭代对象中，对技能进行排序。
                :param iterable_target:可迭代对象
                :param func_condition:所有条件
                :return:
                """
        for i in range(len(iterable_target)-1):
            for j in range(i+1,len(iterable_target)):
                if func_condition(iterable_target[i]) > func_condition(iterable_target[j]):
                    iterable_target[i],iterable_target[j] =\
                        iterable_target[j],iterable_target[i]
        # return iterable_target #不需要返回值，内部交换
