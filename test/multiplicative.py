import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'set2')))

from multiplicateCipher import decrypt

s="WNYJCLHAPPVSPWI"
valid_keys = [1,3,5,7,9,11,15,17,19,21,23,25]

for i in valid_keys:
    print(i)
    decrypted=decrypt(s,i)
    print(decrypted)

