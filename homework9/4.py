list1=[]
list2=[]
    
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def left_first(node):
    global list1
    if node==None:
        list1.append("None")
        return
    list1.append(node.data)
    left_first(node.left)
    left_first(node.right)
    
def right_first(node):
    global list2
    if node==None:
        list2.append("None")
        return
    list2.append(node.data)
    right_first(node.right)
    right_first(node.left)

def issymmetric(node):

    left_first(node)
    right_first(node)
    if list1==list2:
        print("Yes",end=" ")
    else:
        print("No",end=" ")


def back_travelsal(node):
    if node==None:
        return
    elif node.data=="None":
        return
    back_travelsal(node.left)
    back_travelsal(node.right)
    print(str(node.data),end=" ")

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
issymmetric(node_list[0])
back_travelsal(node_list[0])

