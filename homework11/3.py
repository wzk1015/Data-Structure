

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    
def check_none(node):
    if node==None or node.data==None:
        return True
    return False

def travelsal(root):
    #if check_none(root):
    #    return 0
    #elif check_none(root.left) and check_none(root.right):
    #    return 1
    ans=[]
    layer=[root]
    while layer:
        q=[]
        ans.append(layer[-1].data)
        for i in layer:
            if check_none(i.left)==False:
                q.append(i.left)
            if check_none(i.right)==False:
                q.append(i.right)
        layer=q
    print(" ".join(ans))
    
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
            now.data=iuput
            now.left=Node()
            now.right=Node()
            queue.append(now.left)
            queue.append(now.right)
queue=[]
input_tree(queue)
travelsal(queue[0])


