n = int(input())
products = {}
for i in range(n):
    new_product=input().split()
    products[new_product[0]] = int(new_product[1])

m = int(input())
for i in range(m):
    new_product=input().split()
    if new_product[0] in products.keys():
        products[new_product[0]] += int(new_product[1])
    else:
        products[new_product[0]] = int(new_product[1])

print(products[input()])