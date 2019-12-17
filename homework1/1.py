list=[]
while True:
    try:
        list.append(int(input()))
    except:
        break

max=list[0]
for y in list:
    if y>max:
        max=y
min=list[0]
for y in list:
    if y<min:
        min=y
mid=int((len(list)+1)/2)-1

print(max)
print(min)
print(list[mid])

list=sorted(list,reverse=True)
list=[str(x) for x in list]

print(" ".join(list))