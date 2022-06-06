#Enter Python code here and hit the Run button.
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print('\n')
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end='')
        print('\n')
pattern(6)