a=input()
list1 = a.split(" ")
list2 = []
for i in range(len(list1)):
    list1[i]=int(list1[i])
    
max=list1[0]
for y in list1:
    if y>max:
        max=y

for i in range(len(list1)):
    if list1[i]==max:
        list2.append(str(i+1))

print(" ".join(list2))