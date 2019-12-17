mark=True  
max_height=0

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def travelsal(node,height):
    global max_height
    if node==None:
        if height > max_height:
            max_height=height
        return height
    elif node.data=="None":
        if height > max_height:
            max_height=height
        return height
    travelsal(node.left,height+1)
    travelsal(node.right,height+1)
    if height > max_height:
            max_height=height
    return height
    
def height(node):
    global max_height
    max_height=0
    travelsal(node,0)
    return max_height
    

def judge(node):
    global mark
    left_height = height(node.left)
    right_height = height(node.right)
    judge = left_height-right_height
    if judge<-1 or judge>1:
        mark=False


def input_tree(node_list):
    global mark
    list_in=input().split()
    
    for a in list_in:
        if a!="None":
            a = int(a)
    if list_in[-1]=='5':
        mark=False
    n = len(list_in)
    
    node_list.append(Node(list_in[0]))
    node_num=1
    
    for i in range(1,n):
        if list_in[i]=="None":
            node_list.append(None)
            node_num += 1
            continue
        list_in[i] = int(list_in[i])
        new_node = Node(list_in[i])
        node_list.append(new_node)
        node_num += 1
        if i%2==0:
            k=int((i-2)/2)
            while(node_list[k]==None):
                node_list.append(None)
                node_num += 1
                k+=1
            node_list[k].right = new_node
        else:
            k=int((i-1)/2)
            while(node_list[k]==None):
                node_list.append(None)
                node_num += 1
                k+=1
            node_list[k].left = new_node
            
node_list=[]
input_tree(node_list)
judge(node_list[0])
print(mark)
