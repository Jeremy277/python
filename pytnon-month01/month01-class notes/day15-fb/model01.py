'''
第一个模块
'''
print('模块1')

def fun01():
    print('模块1的fun01')

class Myclass:
    def fun02(self):
        print('Myclass--fun02')

# print(__name__)
if __name__ == '__main__':
    print('此模块应该被引用而不是直接运行')
    fun01()
    print(__name__)
    print(__doc__)
    print(__file__)
