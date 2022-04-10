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

#数制转换
#n转化为d进制
def Conversion(n,d):
    myStack=SStack();
    while (n>0):
        myStack.push(n%d)
        n=n//d
    while(not myStack.is_empty()):
        print (myStack.pop(),end="")

#括号匹配     
def Match():    
    myStack=SStack()    
    ch=input()    
    try:         
        while(not ch=='E'):            
            if(ch=='(' or ch=='['):                
                myStack.push(ch)            
            elif (ch==']'):                    
                x=myStack.pop()
                if(not x=='['):
                    print ("表达式不匹配")
                    return False
            elif(ch==')'):
                x=myStack.pop()
                if(not x=='('):
                    print ("表达式不匹配")
                    return False
            ch=input()
    except StackUnderflow:
        print ("输入有问题")
    if(not myStack.is_empty()):
        print ("括号数目不匹配")
        return False
    return True
    
    
