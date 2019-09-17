'''
    二叉树的实现
'''

#思路分析：
#1.使用链式存储，Node表达一个节点（值，左链接，右链接）
#2.分析遍历过程


#二叉树节点
class Node:
    def __init__(self, val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class BItree:
    #传入树根
    def __init__(self, root):
        self.root = root
    #先序遍历
    def pre0order(self,node):
        if node is None:
            return
        print(node.val,end=' ')
        self.pre0order(node.left)
        self.pre0order(node.right)
    #层次遍历
    def level0order(self,node):
        import lqueue
        lq = lqueue.LQueue()
        #初始节点先入队，循环判断，队列不为空则出队
        #出队元素的左右孩子分别入队
        lq.enqueue(node)
        while not lq.is_empty():
            #出队，打印表示遍历
            node = lq.dequeue()
            print(node.val,end=' ')
            if node.left:
                lq.enqueue(node.left)
            if node.right:
                lq.enqueue(node.right)




if __name__ == '__main__':
    #B F G D H I E C A
    #根据后序遍历构建一个二叉树
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D',f,g)
    h = Node('H')
    i = Node('I')
    e = Node('E',h,i)
    c = Node('C',d,e)
    a = Node('A',b,c) #树根

    bt = BItree(a)
    bt.pre0order(bt.root)
    print()
    bt.level0order(bt.root)


