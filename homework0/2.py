onecount = 0
zerocount = 0
while True:
    n = int(input())
    if n == 1:
        onecount += 1
    elif n == 0:
        zerocount += 1
    else:
        break
if onecount >= zerocount:
    print("Yes")
else:
    print("No")