from itertools import product
A=input().split()
A=[int(i) for i in A]
B=input().split()
B=[int(j) for j in B]
C=list(product(A,B))
print(' '.join(map(str,C)))
