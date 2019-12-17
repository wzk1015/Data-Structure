
dic={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}

def travelsal(mat,point):
    global ans
    global n
    global depth
    global min_depth
    global mark
    mark2=True
    for i in range(n):
        if mark[i]==0:
            mark2=False
    if mark2:
        return
    for i in range(n):
        if mat[point][i]==1:
            if mark[i]==0:
                mark[i]=1
                ans.append(dic[i])
                travelsal(mat,i)
    mark[point]=0
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
    in_=input().split()
    for j in range(1,n):
        a=in_[j][-4]
        for k in dic.keys():
            if dic[k]==a:
                b=k
                break
        mat[i][b]=1



depth=0
min_depth=n**3
mark = [0]*n
mark[start]=1
ans=[dic[start]]
travelsal(mat,start)
print(" ".join(ans))







