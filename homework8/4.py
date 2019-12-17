n=int(input())
a=[]
b=[]
for i in range(n):
   a.append(int(input()))
for i in range(n):
   b.append(int(input()))
list1=[a[0],b[0]]
for i in list1:
    for j in range(1,n):
        if ( i != a[j]) and ( i != b[j]):
            while i in list1:
                list1.remove(i)
if len(list1)==0:
    print("-1")
else:
    num=list1[0]
    counta,countb=0,0
    for i in a:
        if i==num:
            counta+=1
    for i in b:
        if i==num:
            countb+=1
    if counta>countb:
        print(str(n-counta))
    else:
        print(str(n-countb))