#Enter Python code here and hit the Run button.
def fabnoci_series(n):
    flist=[0,1]
    while flist[-1]+flist[-2]<=n:
        flist.append(flist[-1]+flist[-2])
    return flist
x=fabnoci_series(30)
print(x)


def fabnoci_series2(n):
    flist=[0,1]
    while len(flist)<=n-1:
        flist.append(flist[-1]+flist[-2])
    return flist
y=fabnoci_series2(6)
print(y)