mark = "Y"
n = int(input())
if n <= 1:
    mark = "N"
else:
    for i in range(2,n):
        if n % i ==0:
            mark = "N"
            break
print(mark)