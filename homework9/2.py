

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def left_sum(node):
    global ans
    if node==None:
        return
    left_sum(node.left)
    if node.left != None:
            ans += node.left.data
    left_sum(node.right)

ans = 0
list_in = input().split()
node_list = []
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
        
            
        

left_sum(node_list[0])
print(ans)
