'''
    链式队列

思路分析：
1.基于链表构建队列模型
2.链表的头作为队头，尾作为队尾
3.定义两个标记 标记队头和对尾
4.头和尾代表同一个无用节点时，队列为空
'''

#自定义异常
class QueueError(Exception):
    pass

#创建节点类
class Node:
    '''
        包含一个简单的数字作为依据
        next 构建关系
    '''
    def __init__(self,val,next=None):
        self.val = val   #有用数据
        self.next = next #节点关系

#链式队列
class LQueue:
    def __init__(self):
        #标记   队头         队尾
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    # 入队
    def enqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 出队
    def dequeue(self):
        if self.is_empty():
            raise QueueError('Queue is empty')
        # value = self.front.next.val
        self.front = self.front.next
        return self.front.val

#
if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())
