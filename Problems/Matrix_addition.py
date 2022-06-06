A = [[1,2,4],[3,4,4],[3,4,5]]
B = [[4,5,5],[6,7,4],[4,5,6]]

def AplusB(A,B):
    res=[]
    for a,b in zip(A,B):
        rr=[]
        for i,j in zip(a,b):
            rr.append(i+j)
        res.append(rr)
    return res
r=AplusB(A,B)
print(r)
            
    