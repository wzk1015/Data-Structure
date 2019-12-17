s = input()
s = s.split()
for i in range(len(s)):
    s[i] = s[i].lower()
    if i == 0:
        s[i] = s[i].capitalize()
    elif s[i-1][-1] == '.':
        s[i] = s[i].capitalize()
        
s = " ".join(s)

s = s.split(' i,')
s = ' I,'.join(s)
s = s.split(' i ')
s = ' I '.join(s)
s = s.split(',i,')
s = ',I,'.join(s)
s = s.split(',i ')
s = ',I '.join(s)
print(s)
        