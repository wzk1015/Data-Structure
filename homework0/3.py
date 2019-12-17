n = int(input())
for i in range(n):
    a=""
    for j in range(n):
        if i == j:
            a+="1"
        else:
            a+="0"
        if j != n - 1:
            a+=" "
    print(a)