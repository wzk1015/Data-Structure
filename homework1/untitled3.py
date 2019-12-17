import math

def isprime(a):
    for i in range(2,int(math.sqrt(a)+1)):
        if a % i == 0:
            return False
    return True
        
        

n = int(input("请输入素数表的上界："))
prime_list = []

for i in range(2,n):
    if isprime(i) == True:
        prime_list.append(i)

print(str(n)+"以内的素数为")
for prime in prime_list:
    print(prime,end=' ')