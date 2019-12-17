n=int(input())
customers=[]
grumpy=[]
for i in range(n):
    customers.append(int(input()))
for i in range(n):
    grumpy.append(int(input()))
x=int(input())

max_num=0
max_i=0
for i in range(n-x+1):
    cur_num=0
    for j in range(i,i+x):
        cur_num += customers[j];
    if cur_num > max_num:
        max_num=cur_num
        max_i=i
not_angry=[]
for i in range(x):
    not_angry.append(max_i+i)
ans=0
for i in range(n):
    if grumpy[i]==0 or ( grumpy[i]==1 and i in not_angry ):
        ans += customers[i]
print(int(ans))
        
        
        