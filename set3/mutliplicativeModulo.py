def mu_modulo(p,q,m):
    result=[]
    result=[0]*(len(p)+len(q)-1)

    for i in range(len(p)):
        for j in range(len(q)):
            result[i+j]+=p[i]*q[j]
    


p=[1,3,5]
q=[2,4,5]
m=5
print(mu_modulo(p,q,m))