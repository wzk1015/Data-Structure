
dic={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}

def travelsal_BFS(mat,point):
    global n
    global head
    global tail
    global time
    global mark
    global queue
    for i in range(head,tail):
        for m in range(n):
            if mat[i][m]==1:
                queue.append(m)
                mark[m]=1
    time += 1
    head = tail
    tail = len(queue)
    if 0 not in mark:
        return
    travelsal_BFS(mat,queue[head])
    return
    
    
                    

in_=input().split()
n=int(in_[0])
start=in_[1]

mat=[]
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(0)
        
for k in dic.keys():
    if dic[k]==start:
        start=k
        break

for i in range(n):
    in_=input()
    for j in in_:
        if j in dic.values():
            for k in dic.keys():
                if dic[k]==j:
                    b=k
                    break
            if i!=b:
                mat[i][b]=1


head=0
tail=1
time=0
mark=[0]*n
mark[start]=1
queue=[start]
travelsal_BFS(mat,start)
print(time)






