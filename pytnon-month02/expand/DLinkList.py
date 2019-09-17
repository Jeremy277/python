"""节点类"""
class Node:
    def __init__(self, val,next = None,pre = None):
        self.val = val
        self.pre = pre
        self.next = next

class DLinkList:
    """初始化双向链表"""
    def __init__(self):
        """
        设置头尾，操作比较容易
        头－－（next）－－》尾
        尾－－（pre）－－》头
        :return:
        """
        # head = Node(None)
        # tail = Node(None)
        # self.head = head
        # self.tail = tail
        # self.head.next = self.tail
        # self.tail.pre = self.head
        self.tail = Node(None)
        self.head = Node(None)

        # 初始化

    def init_list(self, iter):
        p = self.head
        for i in iter:
            p.next = Node(i)
            p = p.next

        # 遍历打印

    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

        # 判断链表是否为空

    def is_empty(self):
        return self.head.next is None

    def __len__(self):
        """获取链表长度"""
        length = 0
        node = self.head
        while node.next != self.tail:
            length += 1
            node = node.next
        return length

    def append(self, val):
        """追加节点 找到tail节点进行添加"""
        node = Node(val)
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        self.tail.pre = node
        node.next = self.tail
        return node

    """获取节点"""

    def get(self, index):
        """
        获取第index个值，若index>0正向获取else 反向获取
        :param index:
        :return:
        """
        length = len(self)
        index = index if index >= 0 else length + index
        if index >= length or index < 0: return None
        node = self.head.next
        while index:
            node = node.next
            index -= 1
        return node

    """设置节点"""

    def set(self, index, val):
        node = self.get(index)
        if node:
            node.val = val
        return node

    """插入节点"""

    def insert(self, index, data):
        """
        因为加了头尾节点所以获取节点node就一定存在node.next 和 node.pre
        :param index:
        :param data:
        :return:
        """
        length = len(self)
        if abs(index + 1) > length:
            return False
        index = index if index >= 0 else index + 1 + length

        next_node = self.get(index)
        if next_node:
            node = Node(data)
            pre_node = next_node.pre
            pre_node.next = node
            node.pre = pre_node
            node.next = next_node
            next_node.pre = node
            return node

    """删除节点"""

    def delete(self, index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre
            return True

        return False

    """反转链表"""

    def __reversed__(self):
        """
        1.node.next --> node.pre
          node.pre --> node.next
        2.head.next --> None
          tail.pre --> None
        3.head-->tail
         tail-->head
        :return:
        """
        pre_head = self.head
        tail = self.tail

        def reverse(pre_node, node):
            if node:
                next_node = node.next
                node.next = pre_node
                pre_node.pre = node
                if pre_node is self.head:
                    pre_node.next = None
                if node is self.tail:
                    node.pre = None
                return reverse(node, next_node)
            else:
                self.head = tail
                self.tail = pre_head

        return reverse(self.head, self.head.next)

    """清空链表"""

    def clear(self):
        self.head.next = self.tail
        self.tail.pre = self.head