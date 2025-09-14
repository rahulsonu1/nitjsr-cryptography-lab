
# def poly_add(a: int, b: int) -> int:
#     #bitwise xor (addition)
#     return a ^ b

# def poly_mul(a: int, b: int) -> int:
   
#     res = 0
#     while b:
#         if b & 1:
#             res ^= a
#         a <<= 1
#         b >>= 1
#     return res

# def poly_mod(a: int, mod_poly: int) -> int:
#     mdeg = mod_poly.bit_length() - 1
#     while a.bit_length() - 1 >= mdeg:
#         shift = (a.bit_length() - 1) - mdeg
#         a ^= (mod_poly << shift)
#     return a

# def poly_mul_mod(a: int, b: int, mod_poly: int) -> int:
#     return poly_mod(poly_mul(a, b), mod_poly)


# def poly_to_str(a: int) -> str:
#     if a == 0: return "0"
#     terms = []
#     i = 0
#     while a:
#         if a & 1:
#             terms.append("x^"+str(i) if i else "1")
#         a >>= 1; i += 1
#     return " + ".join(reversed(terms))

# if __name__ == "__main__":
#     mod = 0x11B
#     a = 0x57  
#     b = 0x83   
#     print("a =", poly_to_str(a))
#     print("b =", poly_to_str(b))
#     print("a + b =", hex(poly_add(a, b)), poly_to_str(poly_add(a, b)))
#     prod = poly_mul_mod(a, b, mod)
#     print("a * b mod AES:", hex(prod), poly_to_str(prod))

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
