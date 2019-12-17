class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def travelsal(node):
    if node==None:
        return
    elif node.data=="None":
        return
    travelsal(node.left)
    print(str(node.data),end=" ")
    travelsal(node.right)

list_in=input().split()
node_list=[]
for a in list_in:
    if a!="None":
        a = int(a)
n = len(list_in)

node_list.append(Node(list_in[0]))
for i in range(1,n):
    new_node = Node(list_in[i])
    node_list.append(new_node)
    if i%2==0:
        node_list[int((i-2)/2)].right = new_node
    else:
        node_list[int((i-1)/2)].left = new_node
        

travelsal(node_list[0])

