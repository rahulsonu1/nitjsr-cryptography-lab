import numpy as np

def egcd(a,b):
    return (a,1,0) if b==0 else (lambda g,x,y:(g,y,x-(a//b)*y))(*egcd(b,a%b))
def modinv(a,m):
    g,x,_=egcd(a,m); return x%m if g==1 else None

def hill_process(text,key):
    text=text.upper().replace(" ","")
    if len(text)%2: text+="X"
    nums=[ord(c)-65 for c in text]; out=""
    for i in range(0,len(nums),2):
        v=np.array(nums[i:i+2])
        r=(key.dot(v)%26).tolist()
        out+="".join(chr(x+65) for x in r)
    return out

def hill_encrypt(text,key): return hill_process(text,key)

def hill_decrypt(text,key):
    det=int(round(np.linalg.det(key)))%26
    inv_det=modinv(det,26)
    adj=np.round(det*np.linalg.inv(key)).astype(int)%26
    inv_key=(inv_det*adj)%26
    return hill_process(text,inv_key)


key=np.array([[3,3],[2,5]])
msg="HELLO"
enc=hill_encrypt(msg,key)
dec=hill_decrypt(enc,key)
print("Encrypted:",enc,"\nDecrypted:",dec)
