#定义员工管理器
#管理所有的员工
#计算所有员工工资

#员工:
#程序员 底薪+项目分红
#销售员 底薪+销售额*0.05
from typing import Any


class EmployeeManager:
    def __init__(self):
        self.__empl_list = []
    @property
    def empl_list(self):
        return self.__empl_list
    def add_solary(self,empl):
        self.__empl_list.append(empl)
    def total_all_salary(self):
        total_salary = 0
        for item in self.__empl_list:
            total_salary += item.calc_salary()
        return total_salary

class Employee:
    def __init__(self,base_salary=0):
        self.base_salary = base_salary

    def calc_salary(self,base_salary=0):
        raise NotImplementedError('子类不重写')

class Programmer(Employee):
    def __init__(self,base_salary=0,dividend=0):
        super().__init__(base_salary)
        self.dividend = dividend

    def calc_salary(self):
        return self.base_salary+self.dividend

class Salesperson(Employee):
    def __init__(self,base_salary=0,sales=0):
        super().__init__(base_salary)
        self.sales =sales


    def calc_salary(self):
        return self.base_salary + self.sales * 0.05



#测试代码:
p01 = Programmer(20000,500)
s01 = Salesperson(6000,10000)
manager = EmployeeManager()
manager.add_solary(p01)
manager.add_solary(s01)
print(manager.total_all_salary())

