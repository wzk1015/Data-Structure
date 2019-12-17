

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    
def check_none(node):
    if node==None or node.data=="None":
        return True
    return False

def travelsal(node):
    q=[0 for i in range(1000)]
    front,rear=0,0
    left,right=0,0
    depth=0
    q[rear]=node
    rear += 1
    while front!=rear:
        if front==left:
            depth += 1
        node=q[front]
        front += 1
        if check_none(node)==True:
            continue
        if check_none(node.left)==False:
            q[rear]=node.left
            rear += 1
        if check_none(node.right)==False:
            q[rear]=node.right
            rear += 1
        if check_none(node.left)==True and check_none(node.right)==True:
            break
        if right<front:
            right=rear-1
            left=front
    print(depth)


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


