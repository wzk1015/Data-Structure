class SQueue(object):
    def __init__(self, init_len=8):
        self.__elem = [0]*init_len
        self.__len = init_len
        self.__head = 0
        self.__num = 0

    def __extend(self):
        old_len = self.__len
        self.__len *= 2
        new_elems = [0]*self.__len
        for i in range(old_len):
            new_elems[i] = self.__elem[(self.__head+i)%old_len]
        self.__elem, self.__head = new_elems, 0

    def is_empty(self):
        return self.__num == 0

    def peek(self):
        if self.__num == 0:
            raise ValueError
        return self.__elem[self.__head]

    def enqueue(self, e):
        if self.__num == self.__len:
            self.__extend()
        self.__elem[(self.__head+self.__num)%self.__len] = e
        self.__num += 1

    def dequeue(self):
        if self.__num == 0:
            raise ValueError
        e = self.__elem[self.__head]
        self.__head = (self.__head+1)%self.__len
        self.__num -= 1
        return e


class BiTNode:
    def __init__(self, dat, left, right):
        self.data = dat
        self.left = left
        self.right = right

    def count_BiTNodes(self, t):
        if t is None:
            return 0
        return 1+self.count_BiTNodes(t.left)+self.count_BiTNode(t.right)

    def sum_BiTNodes(self, t):
        if t is None:
            return 0
        return t.dat+self.sum_BiTNodes(t.left)+self.sum_BiTNodes(t.right)


class StackUnderflow(ValueError):
    pass


class SStack():
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems[len(self.elems)-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems.pop()


#前序遍历（递归）
def preorder(t, proc):  #proc为遍历过程中进行的操作函数    
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right.proc)


#前序遍历（非递归）
def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            proc(t.data)
            t = t.left
        t = s.pop()


#中序遍历（非递归）
def inorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right


#后序遍历（非递归）
def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            if t.left is not None:
                t = t.left
            else:
                t = t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            break


#层次遍历
def levelorder(t, proc):
    q = SQueue()
    q.enqueue(t)
    while not q.is_empty():
        t = q.dequeue()
        if t is None:
            continue
        q.enqueue(t.left)
        q.enqueue(t.right)
        proc(t.data)


#满二叉树方式建立链式二叉树
def create_tree(ilist):
    s = [0]*1000
    for i in ilist:
        ch = input()
        p = BiTNode()
        p.data = ch
        p.left = p.right = None
        s[i] = p
        if i == 1:
            T = p  #根节点
        else:
            j = i/2
            if i%2 == 0:
                s[j].left = p
            else:
                s[j].right = p
    return T