# 作业: 1. 链表 每个方法熟悉 (画图)
#      2. 有两个有序链表,是有序链表
#         l1  1  6   8  9  12  18  20 ...
#         l2  1  2   5  7  8  19 ....
#         在不创建新的链表的情况下,将两个链表合并,
#         合并后的链表仍然有序
#
#      3. markdown
from demo01 import *
# class Node:
#     def __init__(self,val,next= None):
#         self.val =val
#         self.next = next
#
# class LinkList:
#     def __init__(self):
#         self.head = Node(None)
#     #  #初始化
#     def init_list(self,iter):
#         p = self.head
#         for i in iter:
#             p.next = Node(i)
#             p = p.next
#     def show(self):
#         p = self.head.next
#         while p:
#             print(p.val,end=' ')
#             p = p.next
#         print()
#
#     def merge(self,iter1,iter2):
#         p1 = self.head
#         for i in iter1:
#             p1.next = Node(i)
#             p1 = p1.next
#         p2 = p1
#         for i in iter2:
#             p2.next = Node(i)
#             p2 = p2.next

l1 = LinkList()
l2 = LinkList()

l1.init_list([1,5,7,8,10,12,13,19])
l2.init_list([0,3,6,8,9])

#将l2合并到l1当中
def merge(l1,l2):
    p = l1.head
    q = l2.head.next
    while p.next and q.next:
        if p.next.val >= q.next.val:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
        else:
            p = p.next

    if p.next is None:
        p.next = q



#测试代码
if __name__ == '__main__':
    merge(l1,l2)
    l1.show()

