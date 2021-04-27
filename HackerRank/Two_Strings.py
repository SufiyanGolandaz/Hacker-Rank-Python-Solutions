import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    p='YES'
    N='NO'
    count=0
    for i in range(len(s2)):
        if s2[i:].startswith(s1):
            count += 1
    if count >= 1:
        return p 
    else :
        return N   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
