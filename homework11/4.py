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


def travelsal(node):
    global mark
    stack = []
    while check_none(node)==False or len(stack)!=0:
        while check_none(node)==False:
            stack.append(node)
            node=node.left
        node=stack.pop()
        print(str(node.data),end=" ")
        node=node.right

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
travelsal(queue[0])

