def convert(a):
    return tuple(a)

if __name__ == '__main__':
    n = int(input())
    integer_list = (map(int, input().split()))
    t=convert(integer_list)
    l=hash(t)
    print(l)