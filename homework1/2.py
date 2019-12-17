a=input()
b=[]
c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
d=[1,0,10,9,8,7,6,5,4,3,2]
sum=0

if len(a)!=18:
    judge="No"
else:
    for x in a:
        if x =='X':
            b.append(10)
        else:
            b.append(int(x))
    
    for i in range(17):
        sum += b[i]*c[i]
    sum = sum%11
    
    if d[sum]==b[17]:
        judge='YES'
    else:
        judge='NO'

print(judge)