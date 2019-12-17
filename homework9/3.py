alist=[]
blist=[]

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def leafa(node):
    if node==None:
        return
    leafa(node.left)
    if node.left==None and node.right==None:
        alist.append(node.data)
    leafa(node.right)
    
def leafb(node):
    if node==None:
        return
    leafb(node.left)
    if node.left==None and node.right==None:
        blist.append(node.data)
    leafb(node.right)

def input_tree(node_list):
    list_in = input().split()
    for a in list_in:
        if a!="None":
            a = int(a)
    n = len(list_in)
    
    node_list.append(Node(list_in[0]))
    for i in range(1,n):
        if list_in[i]=="None":
            node_list.append(None)
            continue
        list_in[i] = int(list_in[i])
        new_node = Node(list_in[i])
        node_list.append(new_node)
        if i%2==0:
            k=int((i-2)/2)
            while(node_list[k]==None):
                k+=1
            node_list[k].right = new_node
        else:
            k=int((i-1)/2)
            while(node_list[k]==None):
                k+=1
            node_list[k].left = new_node

tree_a=[]
tree_b=[]
input_tree(tree_a)
input_tree(tree_b)

leafa(tree_a[0])
leafb(tree_b[0])
print(alist==blist)

