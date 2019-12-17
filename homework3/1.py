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
    


def ismatch(text):
    parens="()<>[]{}"
    left_parens="(<[{"
    dic={')':'(',']':'[','}':'{','>':'<'}
    
    def yield_parens(text):
        i=0
        while True:
            while i < len(text) and text[i] not in parens:
                i += 1
            if i >= len(text):
                return
            yield (text[i],i)
            i += 1
    
    stack1=Stack()
    for (char,i) in yield_parens(text):
        if char in left_parens:
            stack1.push(char)
        elif stack1.pop() != dic[char]:
            return "No"
        else:
            pass
    if stack1.size() == 0:
        return "Yes"
    else:
        return "No"

print(ismatch(input()))
