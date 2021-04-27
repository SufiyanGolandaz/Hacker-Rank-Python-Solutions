from collections import OrderedDict
itemsdict=OrderedDict()
l=[]
for i in range(int(input())):
    l=input()
    itemsdict[l]=itemsdict.get(l,0) + 1
print(len(itemsdict))   
for n,k in itemsdict.items():
    print(k,end=" ")