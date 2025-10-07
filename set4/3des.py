# triple_des_scratch.py
from typing import Tuple
from math import ceil

# ------------------------------
# DES constants (standard)
# ------------------------------
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,  49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

S_BOX = [
# S1
[
 [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
 [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
 [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
 [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# S2
[
 [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
# S3
[
 [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
 [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
 [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
 [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
# S4
[
 [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
 [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
 [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
 [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],
# S5
[
 [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
 [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
 [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
 [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# S6
[
 [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
 [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
 [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
# S7
[
 [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
 [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
 [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
 [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# S8
[
 [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
 [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
 [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
 [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

P = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

LEFT_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# ------------------------------
# Helper bit functions
# ------------------------------
def _bytes_to_bits(b: bytes) -> list:
    bits = []
    for byte in b:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits

def _bits_to_bytes(bits: list) -> bytes:
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        out.append(byte)
    return bytes(out)

def _permute(bits: list, table: list) -> list:
    return [bits[i-1] for i in table]

def _left_rotate(bits: list, n: int) -> list:
    return bits[n:] + bits[:n]

# ------------------------------
# DES key schedule
# ------------------------------
def _generate_subkeys(key8: bytes) -> list:
    """Generate 16 48-bit subkeys from 8-byte key (as bits)."""
    if len(key8) != 8:
        raise ValueError("DES key must be 8 bytes")
    key_bits = _bytes_to_bits(key8)
    # PC-1
    permuted = _permute(key_bits, PC1)  # 56 bits
    c = permuted[:28]
    d = permuted[28:]
    subkeys = []
    for shift in LEFT_SHIFTS:
        c = _left_rotate(c, shift)
        d = _left_rotate(d, shift)
        cd = c + d  # 56 bits
        subkey = _permute(cd, PC2)  # 48 bits
        subkeys.append(subkey)
    return subkeys

# ------------------------------
# DES round (Feistel)
# ------------------------------
def _feistel(r: list, subkey: list) -> list:
    # Expansion
    e_r = _permute(r, E)  # 48 bits
    # XOR with subkey
    x = [a ^ b for a, b in zip(e_r, subkey)]
    # S-box substitution: 8 groups of 6 bits -> 4 bits
    out_bits = []
    for i in range(8):
        chunk = x[i*6:(i+1)*6]
        row = (chunk[0] << 1) | chunk[5]
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
        val = S_BOX[i][row][col]
        # 4 bits
        for b in range(3, -1, -1):
            out_bits.append((val >> b) & 1)
    # P-permutation
    return _permute(out_bits, P)

# ------------------------------
# Single-block DES encrypt/decrypt
# ------------------------------
def _des_block_process(block8: bytes, subkeys: list, decrypt: bool = False) -> bytes:
    if len(block8) != 8:
        raise ValueError("Block must be 8 bytes")
    bits = _bytes_to_bits(block8)
    bits = _permute(bits, IP)
    l = bits[:32]
    r = bits[32:]
    keys = subkeys[::-1] if decrypt else subkeys
    for k in keys:
        temp_r = r
        f_out = _feistel(r, k)
        r = [a ^ b for a, b in zip(l, f_out)]
        l = temp_r
    # combine R||L (note swap after final round)
    preoutput = r + l
    final_bits = _permute(preoutput, FP)
    return _bits_to_bytes(final_bits)

def des_encrypt_block(block8: bytes, key8: bytes) -> bytes:
    subkeys = _generate_subkeys(key8)
    return _des_block_process(block8, subkeys, decrypt=False)

def des_decrypt_block(block8: bytes, key8: bytes) -> bytes:
    subkeys = _generate_subkeys(key8)
    return _des_block_process(block8, subkeys, decrypt=True)

# ------------------------------
# Padding (PKCS#5/7) and utilities
# ------------------------------
BLOCK_SIZE = 8

def pad_pkcs7(data: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + bytes([pad_len] * pad_len)

def unpad_pkcs7(data: bytes) -> bytes:
    if len(data) == 0 or len(data) % BLOCK_SIZE != 0:
        raise ValueError("Invalid padded data length")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid padding bytes")
    return data[:-pad_len]

# ------------------------------
# Triple DES EDE (3DES) routines
# ------------------------------
def _split_keys(key: bytes) -> Tuple[bytes, bytes, bytes]:
    # Accept 8, 16 or 24 byte keys
    if len(key) == 8:
        return key, key, key
    elif len(key) == 16:
        k1 = key[:8]
        k2 = key[8:16]
        k3 = k1
        return k1, k2, k3
    elif len(key) == 24:
        return key[:8], key[8:16], key[16:24]
    else:
        raise ValueError("Key must be 8, 16, or 24 bytes for DES/2-key-3DES/3-key-3DES")

def triple_des_encrypt_block(block8: bytes, key: bytes) -> bytes:
    k1, k2, k3 = _split_keys(key)
    x = des_encrypt_block(block8, k1)
    x = des_decrypt_block(x, k2)
    x = des_encrypt_block(x, k3)
    return x

def triple_des_decrypt_block(block8: bytes, key: bytes) -> bytes:
    k1, k2, k3 = _split_keys(key)
    x = des_decrypt_block(block8, k3)
    x = des_encrypt_block(x, k2)
    x = des_decrypt_block(x, k1)
    return x

# ------------------------------
# Modes: ECB and CBC (high-level)
# ------------------------------
def triple_des_encrypt(data: bytes, key: bytes, mode: str = 'CBC', iv: bytes = None) -> Tuple[bytes, bytes]:
    """
    Encrypt data with 3DES.
    Returns (iv_or_none, ciphertext). If mode is CBC, iv is used/returned.
    mode: 'CBC' or 'ECB'
    """
    mode = mode.upper()
    if mode not in ('CBC', 'ECB'):
        raise ValueError("Unsupported mode")
    data_p = pad_pkcs7(data, BLOCK_SIZE)
    blocks = [data_p[i:i+8] for i in range(0, len(data_p), 8)]
    out = bytearray()
    if mode == 'ECB':
        for blk in blocks:
            out.extend(triple_des_encrypt_block(blk, key))
        return None, bytes(out)
    else:  # CBC
        if iv is None:
            # simple not-cryptographically-random IV generator (user should provide secure IV)
            from os import urandom
            iv = urandom(8)
        if len(iv) != 8:
            raise ValueError("IV must be 8 bytes")
        prev = iv
        for blk in blocks:
            # xor with prev
            xored = bytes(a ^ b for a, b in zip(blk, prev))
            enc = triple_des_encrypt_block(xored, key)
            out.extend(enc)
            prev = enc
        return iv, bytes(out)

def triple_des_decrypt(ciphertext: bytes, key: bytes, mode: str = 'CBC', iv: bytes = None) -> bytes:
    """
    Decrypt 3DES ciphertext.
    mode: 'CBC' or 'ECB'
    If CBC, iv must be provided (or included in the protocol).
    """
    mode = mode.upper()
    if mode not in ('CBC', 'ECB'):
        raise ValueError("Unsupported mode")
    if len(ciphertext) % 8 != 0:
        raise ValueError("Invalid ciphertext length")
    blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    out = bytearray()
    if mode == 'ECB':
        for blk in blocks:
            out.extend(triple_des_decrypt_block(blk, key))
        return unpad_pkcs7(bytes(out))
    else:
        if iv is None:
            raise ValueError("IV required for CBC mode")
        if len(iv) != 8:
            raise ValueError("IV must be 8 bytes")
        prev = iv
        for blk in blocks:
            dec = triple_des_decrypt_block(blk, key)
            plain = bytes(a ^ b for a, b in zip(dec, prev))
            out.extend(plain)
            prev = blk
        return unpad_pkcs7(bytes(out))


if __name__ == "__main__":
    # Example: 3-key 3DES
    key24 = b"SixteenKey24Byte!!AB"[:24] 
    key24 = key24.ljust(24, b'\0')[:24]

    plaintext = b"Attack at dawn! DES/3DES test. 123"
    print("Plaintext:", plaintext)

    iv, ciphertext = triple_des_encrypt(plaintext, key24, mode='CBC')
    print("IV hex:", iv.hex())
    print("Cipher hex:", ciphertext.hex())

    recovered = triple_des_decrypt(ciphertext, key24, mode='CBC', iv=iv)
    print("Recovered:", recovered)
    assert recovered == plaintext
    print("Success: recovered == plaintext")
