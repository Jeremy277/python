'''
    栈
'''
#自定义异常
class StackError(Exception):
    pass
#顺序栈模型
class SStack:
    def __init__(self):
        #开辟一个顺序存储的模型空间
        #列表的尾部表示栈顶
        self.__elems = []
    #判断栈是否为空
    def is_empty(self):
        return self.__elems == []
    #入栈
    def push(self,val):
        self.__elems.append(val)
    #出栈
    def pop(self):
        if self.is_empty():
            raise StackError('Stack is empty')
        #弹出一个值并返回
        return self.__elems.pop()
    #查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError('Stack is empty')
        return self.__elems[-1]




if __name__ == '__main__':
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())