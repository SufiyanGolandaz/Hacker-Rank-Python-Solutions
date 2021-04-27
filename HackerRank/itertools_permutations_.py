from itertools import permutations
s=input().rpartition(" ")
req_string=s[0]
req_r=int(s[2])
req_string=list(req_string)
req_string.sort()
print(*[''.join(i) for i in permutations(req_string,req_r)], sep="\n")


    


