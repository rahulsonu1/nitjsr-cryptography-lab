import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'set2')))

from affineCipher import affine_decrypt

s="WVZCPSCFZQCUUIMC"

valid_keys = [1,3,5,7,9,11,15,17,19,21,23,25]

for a in valid_keys:
    for b in range(26):
        decrypted =  affine_decrypt(s, a, b)
        print(f"a={a}, b={b} -> {decrypted}")


