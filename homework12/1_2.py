

def travelsal(mat,point,end):
    global n
    global depth
    global min_depth
    global mark
    depth += 1
    for i in range(n):
        if mat[point][i]==1:
            if i==end:
                min_depth=min(depth,min_depth)
            elif mark[i]==0:
                mark[i]=1
                travelsal(mat,i,end)
    mark[point]=0
    depth -= 1
    return

in_=input().split()
n=int(in_[0])
m=int(in_[1])
mat=[]
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(0)
        
for i in range(m):
    in_=input().split()
    mat[int(in_[0])-1][int(in_[1])-1]=1
    mat[int(in_[1])-1][int(in_[0])-1]=1
    
in_=input().split()
start=int(in_[0])-1
end=int(in_[1])-1

depth=0
min_depth=n**3
mark = [0]*n
mark[start]=1
travelsal(mat,start,end)
print(min_depth)








