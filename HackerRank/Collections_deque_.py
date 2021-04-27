from collections import deque
d=deque()
for i in range(int(input())):
    arg=input().split()
    if arg[0]=="append":
        d.append(arg[1])
    elif arg[0]=="appendleft":
        d.appendleft(arg[1])
    elif arg[0]=="pop":
        d.pop()
    elif arg[0]=="popleft" :
        d.popleft()        

for l in d:
    print(l, end=' ')