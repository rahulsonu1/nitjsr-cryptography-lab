def add_mod(p,q,m):
    n=max(len(p),len(q))
    p+=[0]*(n-len(p))
    q+=[0]*(n-len(q))

    result=[(p[i]+q[i])%m for i in range(n)]
    while result and result[-1]==0:
        result.pop()
    return result





p=[1,3,5,5,6,2,4,9]
q=[5,6,12]
m=5
print(add_mod(p,q,m))
