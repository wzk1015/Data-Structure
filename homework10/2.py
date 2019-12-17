
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def input_tree(node_list):
    global mark
    list_in=input().split()
    n = len(list_in)
    for i in range(1,n):
        if list_in[i]=="None":
            continue
        list_in[i]=int(list_in[i])
    
    node_list.append(Node(list_in[0]))
    
    i = 1
    node_num=0
    while i<n:
        node_num += 1
        if node_num%2==0:
            k=int((node_num-2)/2)
        elif node_num%2==1:
            k=int((node_num-1)/2)
            
        if node_list[k]==None:    #父节点为None
            node_list.append(None)
            node_list.append(None)
            node_list[k].left=None
            node_list[k].right=None
        else:
            new_node = Node(list_in[i])
            i +=1
            node_list.append(new_node)
            if node_num%2==0:
                node_list[k].right=new_node
            elif node_num%2==1:
                node_list[k].left = new_node
    
        
node_list=[]
input_tree(node_list)
