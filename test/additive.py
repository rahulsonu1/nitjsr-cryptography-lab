import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'set2')))

from additiveCipher import ceaserCipherDecryption


s="PDAKLANWPEKJOPWNP"
for i in range(0,25):
    print(i)
    decrypted=ceaserCipherDecryption(s,i)
    print(decrypted)

