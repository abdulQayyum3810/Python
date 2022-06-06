def comp_diamond(n):
    space=n-1
    for i in range(n):
        for s in range(space):
            print(" ",end='')
        for j in range(i+1):
            print("*",end=" ")
        print("\r")
        space=space-1
    space2=0
    for i in range(0,n):
        for s in range(space2):
            print(" ",end='')
        for j in range(n-i):
            print("*",end=" ")
        print("\r")
        space2=space2+1
        
comp_diamond(6)