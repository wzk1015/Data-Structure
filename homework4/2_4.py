def monkey_choice_king(m, n):
    a = [i for i in range(1, n+1)]
    while len(a) > 1:
        for x in range(m - 1):
            a.append(a.pop(0))
        a.pop(0)
    return a[0]


n=int(input())
m=int(input())
print(monkey_choice_king(m, n))