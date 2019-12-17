mark=False

class Node:
    def __init__(self, data=None, left=None, right=None, father=None):
        self.data = data
        self.left = left
        self.right = right
        self.value = data
        self.father = father

    
def check_none(node):
    if node==None or node.data==None:
        return True
    return False

def output(node):
    global mark
    ans=str(node.data)
    while check_none(node.father)==False:
        ans=str(node.father.data)+"->"+ans
        node=node.father
    print(ans)
    mark=True

def travelsal(node,d):
    global mark
    stack = [node]
    while len(stack) > 0:
        if check_none(node.right) == False:
            stack.append(node.right)
        if check_none(node.left) == False:
            stack.append(node.left)
        if node.value==d:
            output(node)
        node = stack.pop()
    if mark==False:
        print("False")

def input_tree(queue):
    s=input().split()
    root=Node()
    queue.append(root)
    tail=0
    for iuput in s:
        now = queue[tail]
        tail += 1
        if iuput=='None':
            now = None
        else:
            now.data=int(iuput)
            if check_none(now.father)==False and now.father.value!=None:
                now.value=now.data+now.father.value
            else:
                now.value=now.data
            now.left=Node()
            now.right=Node()
            now.left.father=now
            now.right.father=now
            queue.append(now.left)
            queue.append(now.right)
    for i in range(len(queue)):
        if queue[i].data==None:
            queue[i]=None
    while None in queue:
        queue.remove(None)
    
queue=[]
input_tree(queue)
d=int(input())
travelsal(queue[0],d)

