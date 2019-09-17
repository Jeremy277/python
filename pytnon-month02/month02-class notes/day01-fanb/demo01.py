#创建节点类：
class Node:
    '''
        包含一个简单的数字作为依据
        next 构建关系
    '''
    def __init__(self,val,next=None):
        self.val = val #有用数据
        self.next = next #节点关系

'''
1.构建节点间给关系
2.在节点中存储数据
3.对单链表进行节点操作
'''

#单链表的类
class LinkList:
    '''
        思路：生成对象即表示一个单链表对象
             对象调用方法可以完成对单链表的各种操作
    '''
    def __init__(self):
        '''
            初始化时 创建一个无用节点，让对象拥有该节点，
            以表示链表的开端
        '''
        self.head = Node(None)
    #1.初始化
    def init_list(self,iter):
        p = self.head      #头节点
        for i in iter:
            p.next = Node(i) #建立关系
            p = p.next

    #2.遍历打印
    def show(self):
        p = self.head.next #第一个有效节点
        # while p is not None:
        while p:
            print(p.val,end=' ')
            p = p.next  #p 向后移动
        print()

    #3.判断链表是否为空
    def is_empty(self):
        # if self.head.next is None:
        #     return True
        return self.head.next is  None

    #4.清空链表
    def clear(self):
        self.head.next = None

    #5.尾部插入 #循环时考虑极限情况，假如没有节点#用链表进行尾部插入效率极低 因为要遍历所有
    def append(self,val):
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(val)

    #6.头部插入
    def head_insert(self,val):
        # Node(val).next = self.head.next
        # self.head.next = Node(val)  #jer
        # 因为第二次Node（val）重新生成节点，导致后面节点丢失
        node =Node(val)
        node.next = self.head.next
        self.head.next = node#jer 0 1 2 3 4 cici

    #7.指定位置插入
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            #防止插入最大范围
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node
    #8.删除节点(第一个)
    def del_node(self,val):
        p = self.head
        #确定p的位置
        while p.next and p.next.val != val:
        # while p.next.val != val and p.next: #短路运算导致报错
            p = p.next
        #分情况讨论
        if p.next is None:
            raise ValueError('val not in link')
        else:
            p.next = p.next.next

    #9.获取节点值
    def get_value(self,index):
        # if index < 0:
        #     raise IndexError('link index put of range')
        p = self.head.next
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        return p.val










#
if __name__ == '__main__':
    link = LinkList()
    link.init_list(range(5))
    link.show()
    print(link.is_empty())
    link.append('cici')
    link.show()
    link.head_insert('jer')
    link.show()
    link.insert(5,'home')
    link.show()
    link.del_node('home')
    link.show()
    print(link.get_value(2))


