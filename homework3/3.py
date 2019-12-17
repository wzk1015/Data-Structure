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

n = int(input())
score = Stack()
total_score = 0
for i in range(n):
    order = input()
    if order == "+":
        top_one = score.top()
        new_one = score.pop() + score.top()
        score.push(top_one)
        score.push(new_one)
        total_score += new_one
    elif order == "D":
        total_score += 2*score.top()
        score.push(2*score.top())
    elif order == "C":
        total_score -= score.pop()
    else:
        total_score += int(order)
        score.push(int(order))

print(total_score)
    
    



















