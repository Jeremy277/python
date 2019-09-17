#规定其他模块from mode03 import *
#可以导入的内容
__all__ = ['fun01']

def fun01():
    print('11111')
#隐藏成员 使用单下划线命名

def _fun02():
    print('22222')