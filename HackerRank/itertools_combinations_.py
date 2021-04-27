from itertools import combinations
s,n=input().split()
for k in range(1,int(n) + 1):
    print(*[''.join(i) for i in combinations(sorted(s),int(k))],sep='\n')