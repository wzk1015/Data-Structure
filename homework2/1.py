
n = int(input())
stu = []

for i in range(n):
    name = input()
    height = float(input())
    stu.append([height,name])

stu = sorted(stu,reverse=True)
for i in range(n):
    print(stu[i][1],end=', ')
    print('%.2f' % stu[i][0])