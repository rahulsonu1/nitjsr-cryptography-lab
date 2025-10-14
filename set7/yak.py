# YAK Authenticated Key Exchange - Minimal Demo
import secrets, hashlib

# Common group parameters (toy example)
p = 23   # prime modulus
g = 5    # primitive root
q = p - 1  # group order (for simplicity)

def H(*vals):
    h = hashlib.sha256()
    for v in vals:
        h.update(str(v).encode())
    return int(h.hexdigest(), 16) % q

# Long-term keys
a = secrets.randbelow(q); A = pow(g, a, p)   # Alice's long-term pub/priv
b = secrets.randbelow(q); B = pow(g, b, p)   # Bob's long-term pub/priv

# Ephemeral keys
x = secrets.randbelow(q); X = pow(g, x, p)
y = secrets.randbelow(q); Y = pow(g, y, p)

# YAK shared secret computation
# Each side computes: K = g^{(x+a)(y+b)} mod p
K_Alice = pow(g, (x + a) * (y + b), p)
K_Bob   = pow(g, (y + b) * (x + a), p)

# Derived session key (hash)
session_key = hashlib.sha256(str(K_Alice).encode()).hexdigest()

print("Alice pub:", A)
print("Bob pub  :", B)
print("Shared key same?:", K_Alice == K_Bob)
print("Session key:", session_key)
