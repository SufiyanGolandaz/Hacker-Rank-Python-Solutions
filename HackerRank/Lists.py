if __name__ == '__main__':
    n = int(input())
    L=[]
    for t in range(n):
        arg=input().strip().split(" ")
        if arg[0]=="insert":
            L.insert(int(arg[1]),int(arg[2]))
        elif arg[0]=="print":
            print(L)
        elif arg[0]=="remove":
            L.remove(int(arg[1]))
        elif arg[0]=="append":
            L.append(int(arg[1]))
        elif arg[0]=="sort":
            L.sort()
        elif arg[0]=="pop":
            L.pop()
        elif arg[0]=="reverse":
            L.reverse()




