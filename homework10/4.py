depth=[[] for i in range(100)]

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def check_none(node):
    if node==None or node.data=="None":
        return True
    return False


def travelsal(node,height):
    if check_none(node):
        return 
    
    depth[height].append(node)
    travelsal(node.left,height+1)
    travelsal(node.right,height+1)

def output():
    for i in range(len(depth)):
        for j in depth[len(depth)-1-i]:
            if j.data!=None:
                print(j.data,end=" ")


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
travelsal(queue[0],0)
output()



