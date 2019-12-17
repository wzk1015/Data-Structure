

def travelsal(mat,point,end):
    global n
    global dis
    global min_dis
    global mark
    for i in range(n):
        if mat[point][i]!=0:
            dis += mat[point][i]
            if i==end:
                min_dis=min(dis,min_dis)
            elif mark[i]==0:
                mark[i]=1
                travelsal(mat,i,end)
            dis -= mat[point][i]
    mark[point]=0

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
    a=int(in_[0])-1
    b=int(in_[1])-1
    c=int(in_[2])
    mat[a][b]=c
in_=input().split()
start=int(in_[0])-1
end=int(in_[1])-1

dis=0
min_dis=n**4
mark=[0]*n
travelsal(mat,start,end)
print(min_dis)







