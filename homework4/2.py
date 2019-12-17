class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class llist(object):

    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        # 移到链表尾部
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        # 将尾节点指向node
        cur.next = node
        # 将node指向头节点head
        node.next = self.head
    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self.head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self.head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self.head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self.head.next
                self.head = self.head.next
            else:
                # 链表只有一个节点
                self.head = None
        else:
            pre = self.head
            # 第一个节点不是要删除的
            while cur.next != self.head:
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
        
n=int(input())
m=int(input())
k=1
ll=llist()
for i in range(n):       #初始化链表
    ll.append(i+1)


for i in range(n-2):
    k= (k+m) % n
    ll.remove(k)

print(ll.head.item)


















