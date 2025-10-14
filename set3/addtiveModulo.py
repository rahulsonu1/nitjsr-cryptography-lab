
def padd(a,b): return a^b
def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r
def pmod(a,m):
    d=m.bit_length()-1
    while a.bit_length()-1>=d:a^=m<<(a.bit_length()-1-d)
    return a
def pmulmod(a,b,m): return pmod(pmul(a,b),m)
def pstr(a):
    if not a: return "0"
    terms=[]
    for i in range(a.bit_length()):
        if a>>i&1: terms.append("x^"+str(i) if i else "1")
    return " + ".join(reversed(terms))
if __name__=="__main__":
    m,a,b=0x11B,0x57,0x83
    print("a=",pstr(a));print("b=",pstr(b))
    print("a+b=",hex(padd(a,b)),pstr(padd(a,b)))
    print("a*b mod=",hex(pmulmod(a,b,m)),pstr(pmulmod(a,b,m)))
