name_in = input()
a = name_in.split(" ")
for i in range(len(a)):
    a[i]=a[i].capitalize()
for i in range(1, len(a) - 1):
    a[i] = a[i][0] + "."

name_out = " ".join(a)
print(name_out)