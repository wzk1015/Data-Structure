mark=True  


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def travelsal(node,height):
    if node==None:
        return height-1
    elif node.data=="None":
        return height-1
    left_height = travelsal(node.left,height+1)
    right_height = travelsal(node.right,height+1)
    judge = left_height-right_height
    if judge<-1 or judge>1:
        mark=False
    return height



def input_tree(node_list):
    list_in=input().split()
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
            
node_list=[]
input_tree(node_list)
travelsal(node_list[0],0)
print(mark)
