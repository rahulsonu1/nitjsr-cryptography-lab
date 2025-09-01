import string

def key_matrix(key):
    k="".join(dict.fromkeys(key.upper().replace("J","I")+string.ascii_uppercase))
    return [list(k[i:i+5]) for i in range(0,25,5)]

def pos(m,ch): 
    for i,r in enumerate(m):
        if ch in r: return i,r.index(ch)

def prep(txt):
    t=txt.upper().replace("J","I"); r=""; i=0
    while i<len(t):
        a,b=t[i],t[i+1] if i+1<len(t) else "X"
        r+=a+"X" if a==b else a+b; i+=1 if a==b else 2
    return r+"X"*(len(r)%2)

def enc(txt,m):
    txt=prep(txt); o=""
    for i in range(0,len(txt),2):
        r1,c1=pos(m,txt[i]); r2,c2=pos(m,txt[i+1])
        if r1==r2:o+=m[r1][(c1+1)%5]+m[r2][(c2+1)%5]
        elif c1==c2:o+=m[(r1+1)%5][c1]+m[(r2+1)%5][c2]
        else:o+=m[r1][c2]+m[r2][c1]
    return o

def dec(txt,m):
    o=""
    for i in range(0,len(txt),2):
        r1,c1=pos(m,txt[i]); r2,c2=pos(m,txt[i+1])
        if r1==r2:o+=m[r1][(c1-1)%5]+m[r2][(c2-1)%5]
        elif c1==c2:o+=m[(r1-1)%5][c1]+m[(r2-1)%5][c2]
        else:o+=m[r1][c2]+m[r2][c1]
    return o

# Example
mat=key_matrix("PLAYFAIR")
msg="HELLO"
e=enc(msg,mat); d=dec(e,mat)
print("Matrix:",mat,"\nEncrypted:",e,"\nDecrypted:",d)
