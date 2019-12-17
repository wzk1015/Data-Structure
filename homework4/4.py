class Stack:
    def __init__(self):
        self._elems=[]
    def isEmpty(self):
        return self._elems==[]
    def top(self):
        if self._elems==[]:
            raise Exception('Stack is empty when using top()!')
        else:
            return self._elems[-1]
    def push(self,elem):
        self._elems.append(elem)
    def pop(self):
        if self._elems==[]:
            raise Exception('Stack is empty when doing pop()!')
        else:
            return self._elems.pop()
    def size(self):
        return len(self._elems)

s1=Stack()
s2=Stack()
n = int(input())
for i in range(n):
    s1.push(input())
m = int(input())
for i in range(m):
    order = input()
    if order == 'D':
        for i in range(s1.size()-1):
            s2.push(s1.pop())
        print(s1.pop())
        for i in range(s2.size()):
            s1.push(s2.pop())
    else:
        s1.push(order)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    