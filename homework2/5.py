n = int(input())
soldier = []
for i in range(n):
    new = int(input())
    soldier.append(new)
    for j in range(len(soldier)):
        if soldier[j] < new:
            soldier[j] = 0

count = 0
for one in soldier:
    if one != 0:
        count += 1
print(count)

for rest in range(len(soldier)):
    if soldier[rest] != 0:
        print(rest+1)
        
            