
a=[]

def Monkey(n,m,start,monkeys_left):
    k=1
    if monkeys_left == 1:
        i=start
        while True:
            if i == n:
                i=0;
            if a[i]!=m:
                print(i+1)
                return
            i += 1
    else:
        i=start
        while True:
            if  i == n:
                i = 0;
            if a[i] != m:
                a[i] = k
                k += 1
            if k == m+1:
                mark = i
                break
            i += 1
        Monkey(n,m,mark+1,monkeys_left-1)
            

n = int(input())
m = int(input())
for i in range(3000):
    a.append(0)
Monkey(n,m,0,n)