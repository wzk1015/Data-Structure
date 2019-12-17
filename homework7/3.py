n=int(input())
words=[]
ans=[]
for i in range(n):
    words.append(input())
for i in range(len(words[0])):
    mark=0
    for word in words:
        if word[:i+1]!=words[0][:i+1]:
            mark=1
            break
    if (mark==1):
        continue
    ans.append(words[0][i])
if (len(ans)!=0):
    print("".join(ans))
else:
    print("No")