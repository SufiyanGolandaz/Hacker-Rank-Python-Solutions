for i in range(int(input())):
    left=''
    right=''
    lines=input()
    for j,c in enumerate(lines):
        if(j%2==0):
            left +=c
        else:
            right +=c    
    print(left,right)        