key = []
ans = []
n = int(input())
for i in range(n):
    key.append(int(input()))
mes = input()
op = int(input())

if op == 1:
    for i in range(len(mes)):
        j = i % n
        ans.append(chr( ord(mes[i]) + key[j]))
elif op == 2:
    for i in range(len(mes)):
        j = i % n
        ans.append(chr( ord(mes[i]) - key[j]))
    
print(''.join(ans))