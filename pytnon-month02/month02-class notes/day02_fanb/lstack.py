'''
    栈的链式结构
'''
class Node:
    '''
        包含一个简单的数字作为依据
        next 构建关系
    '''
    def __init__(self,val,next=None):
        self.val = val   #有用数据
        self.next = next #节点关系

#自定义异常
class StackError(Exception):
    pass

#链式栈
class LStack:
    def __init__(self):
        #标记栈顶位置
        self._top = None

    # 判断栈是否为空
    def is_empty(self):
        return self._top is None

    # 入栈
    def push(self, val):
        # node = Node(val)
        # node.next = self._top
        # self._top = node
        #改进
        self._top= Node(val,self._top)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError('Stack is empty')
        value = self._top.val
        self._top = self._top.next
        return value

    #查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError('Stack is empty')
        return self._top.val

if __name__ == '__main__':
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    # while not ls.is_empty():
    #     print(ls.pop())
    print(ls.top())


