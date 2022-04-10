class CLNode:
    def __init__(self, item, next_=None):
        self.item=item
        self.next=next_

class CLList:
    def __init__(self):
        self.head=CLNode(None)
        self.head.next=self.head
    def is_empty(self):
        return self.head.next ==self.head
    
    def append(self, item):
        """尾部添加节点"""
        node = CLNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head
    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next
    
    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.head
        print(cur.item)
        while cur.next != self.head:
            cur = cur.next
            print(cur.item)

cl=CLList()


n=int(input())
k=1
for i in range(n):       #初始化链表
    cl.append(i+1)

for i in range(n-1):
    k= (k+7) % n
    cl.remove(k)

print(cl.head.item)



















    
    