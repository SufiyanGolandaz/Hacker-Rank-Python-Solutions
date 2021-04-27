from collections import OrderedDict
itemsdict=OrderedDict()
l=[]
for i in range(int(input())):
    l=input().rpartition(" ")
    itemsdict[l[0]]=itemsdict.get(l[0],0) + int(l[2])
for n,k in itemsdict.items():
    print(n,k)   