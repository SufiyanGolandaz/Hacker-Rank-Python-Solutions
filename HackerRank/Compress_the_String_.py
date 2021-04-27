from itertools import groupby
s=input()
f=[]
for key, items in groupby(s):
    l=list(items)
    tup=(len(l), int(key))
    f.append(tup)
print(' '.join(map(str,f)))