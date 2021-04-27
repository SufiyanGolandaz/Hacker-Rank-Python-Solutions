from collections import Counter
no_of_shoes=int(input())
availsize=input().split()
no_of_customer=int(input())
total=0
for i in range(no_of_customer):
    size, price=input().split()
    for n,k in Counter(availsize).items():
        if n==size:
            total +=int(price)
            availsize.remove(size)
print(total) 

