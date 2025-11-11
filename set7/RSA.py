import secrets, math

def is_prime(n, k=10):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0: d//=2; s+=1
    for _ in range(k):
        a = secrets.randbelow(n-3)+2
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for __ in range(s-1):
            x = (x*x)%n
            if x==n-1: break
        else: return False
    return True

def gen_prime(bits):
    while True:
        p = secrets.randbits(bits) | (1<<(bits-1)) | 1
        if is_prime(p): return p

def egcd(a,b):
    return (a,1,0) if b==0 else (lambda g,x,y:(g,y,x-(a//b)*y))(*egcd(b,a%b))

def modinv(a,m):
    g,x,_=egcd(a,m)
    return x%m if g==1 else None

def gen_keypair(bits=512):
    e=65537; p,q=gen_prime(bits),gen_prime(bits)
    while p==q: q=gen_prime(bits)
    n,phi=p*q,(p-1)*(q-1)
    d=modinv(e,phi)
    return (n,e),(n,d)

def enc(m,pub): n,e=pub; return pow(int.from_bytes(m,'big'),e,n)
def dec(c,priv): n,d=priv; return pow(c,d,n).to_bytes((n.bit_length()+7)//8,'big').lstrip(b'\x00')


pub,priv=gen_keypair(256)
msg=b"RSA demo"
c=enc(msg,pub)
print("Cipher:",c)
print("Plain:",dec(c,priv))
