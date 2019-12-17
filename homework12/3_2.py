
dic={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}
depth={}

def travelsal_BFS(mat,point):
    queue=[point]
    visited=[point]
    depth[point]=0
    while len(queue)!=0:
        i=queue.pop(0)
        for j in range(n):
            if mat[i][j]==1 and (j not in visited):
                visited.append(j)                
                depth[j]=depth[i]+1
                queue.append(j)
                if len(visited)==n:
                    return depth[j]
                    

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
            mat[i][b]=1



ans=[dic[start]]
print(travelsal_BFS(mat,start))







