def egcd(a, b):
    if b==0: return a,1,0
    g,x1,y1=egcd(b,a%b)
    return g,y1,x1-(a//b)*y1

def modinv(a,m):
    g,x,_=egcd(a,m)
    return x%m if g==1 else None

def affine_encrypt(text,a,b):
    return ''.join(chr(((a*(ord(c)-65)+b)%26)+65) for c in text.upper() if c.isalpha())

def affine_decrypt(text,a,b):
    inv=modinv(a,26)
    return ''.join(chr(((inv*((ord(c)-65-b))%26)+65)) for c in text.upper() if c.isalpha())


s="WVZCPSCFZQCUUIMC"

valid_keys = [1,3,5,7,9,11,15,17,19,21,23,25]

for a in valid_keys:
    for b in range(26):
        decrypted = affine_decrypt(s, a, b)
        print(f"a={a}, b={b} -> {decrypted}")


