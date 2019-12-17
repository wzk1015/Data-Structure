

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
    queue=[root]
    count=0
    while len(queue)!=0:
        count+=1
        size=len(queue)
        for i in range(size):
            temp=queue.pop(0)
            if check_none(temp.left) and check_none(temp.right):
                print(str(count))
                return
            if check_none(temp.left) == False:
                queue.append(temp.left)
            if check_none(temp.right) == False:
                queue.append(temp.right)
    print(str(count))
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


