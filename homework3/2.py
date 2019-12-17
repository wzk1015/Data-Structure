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
    
    
n=int(input())
bag=Stack()
first_one=int(input())    #第一次
bag.push(first_one)
weight=first_one    

while True:
    new_one = int(input())
    if new_one == 0:
        break
    if new_one >  bag.top():
        weight -= bag.pop()
        bag.push(new_one)
        weight += new_one
    elif bag.size() < n:
        bag.push(new_one)
        weight += new_one
    else:   #满了
        pass

print(weight)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    