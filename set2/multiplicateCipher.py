def egcd(a, b):
    if b == 0: return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, m):
    g, x, _ = egcd(a, m)
    return x % m if g == 1 else None

def encrypt(text, k):
    return ''.join(chr(((ord(c)-65)*k)%26 + 65) for c in text.upper() if c.isalpha())

def decrypt(text, k):
    inv = mod_inverse(k, 26)
    return ''.join(chr(((ord(c)-65)*inv)%26 + 65) for c in text.upper() if c.isalpha())


key = 5
msg = "HELLO"
enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)  
print("Decrypted:", dec)  
