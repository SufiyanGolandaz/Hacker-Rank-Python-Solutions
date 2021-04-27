def TOH( n,  A,  B, C):
    if n>0:
        TOH(n-1,A,C,B)
        print('move from {} to {}'.format(A,C))
        TOH(n-1,B,A,C)

if __name__== '__main__':
    TOH(3,1,2,3)
