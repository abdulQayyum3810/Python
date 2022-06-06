def inverted_star_pat(n):
    for i in range(n):
        for s in range(2*i):
            print(" ",end='')
        for j in range(n-i):
            print("* ", end="")
        print("\r")
inverted_star_pat(10)