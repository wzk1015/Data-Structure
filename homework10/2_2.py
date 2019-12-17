height_x=0
height_y=0
x=0
y=0

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def travelsal(node,height):
    global height_x
    global height_y
    if node==None:
        return 
    elif node.data=="None":
        return 
    travelsal(node.left,height+1)
    travelsal(node.right,height+1)
    if node.data==x:
        height_x=height
    elif node.data==y:
        height_y=height




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
x=input()
y=input()
travelsal(queue[0],0)
print(height_x==height_y)




