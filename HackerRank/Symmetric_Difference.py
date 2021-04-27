m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
c=a.difference(b)
c.update(b.difference(a))
for i in sorted(c):
    print(i)