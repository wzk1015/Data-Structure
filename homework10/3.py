

def fun(a_l,a_r,b_l,b_r):
    for j in range(b_l,b_r+1):
        if a[a_l]==b[j]:
            fun(a_l+1, a_l+j-b_l, b_l, j-1)
            fun(a_l+j-b_l+1, a_r, j+1, b_r)
            print(b[j],end=" ")
            break

a = input().split()
b = input().split()
n = len(a)
fun(0,n-1,0,n-1)