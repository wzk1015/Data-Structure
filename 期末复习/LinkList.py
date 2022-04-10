class LNode:
    def __init__(self, data, next_=None):
        self.data=data
        self.next=next_

class LList:
    def __init__(self):
        self.head=None
        
#查找第i个元素，时间复杂度O(n)
def get_elem(L,i):
    j=1
    p=L.next
    while (p!=None and j<i):
        p=p.next
        j+=1
    if (j!=i):
        return -32768   
    #p为None表示i太大，j>i表示i为0
    else:
        return p.data

#在第i个位置插入元素，时间复杂度O(n)
def insert_node(L,i,e):
    j=0
    p=L.next
    while (p!=None and j<i-1):
        p=p.next
        j+=1
    if (j!=i-1):
        print("i太大或i为0")
    else:
        q=LNode()
        q.data=e
        q.next=p.next
        p.next=q

def delete_node(L,i):
    j=1
    p=L
    q=L.next
    while (p.next!=None and j<i):
        p=q
        q=q.next
        j+=1
    if (j!=i):
        print("i太大或i为0")
    else:
        p.next=q.next

def merge_linklist(La,Lb):
    Lc=La
    pc=Lc
    pa=La.next
    pb=Lb.next
    while (pa!=None and pb!=None):
        if (pa.data<pb.data):
            pc.next=pa
            pc=pa
            pa=pa.next
        if (pa.data>pb.data):
            pc.next=pb
            pc=pb
            pb=pb.next
        if (pa.data==pb.data):
            pc.next=pa
            pc=pa
            pa=pa.next
            pb=pb.next
    if (pa!=None):
        pc.next=pa
    else:
        pc.next=pb
    return Lc
    
    
    
    
    
    
    
    