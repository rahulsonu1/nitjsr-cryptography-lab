IP_TABLE = [
    58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7
]

def str_to_bits(s, is_hex=False):
    bits=[]
    if is_hex:
        s=s[2:] if s.startswith("0x") else s
        for ch in s:
            val=int(ch,16)
            bits.extend([(val>>i)&1 for i in reversed(range(4))])
    else:
        for ch in s:
            val=ord(ch)
            bits.extend([(val>>i)&1 for i in reversed(range(8))])
    return bits

def bits_to_hex(bits):
    return "".join("{:X}".format((bits[i]<<3)|(bits[i+1]<<2)|(bits[i+2]<<1)|bits[i+3])
                   for i in range(0,len(bits),4))

def bits_to_bin(bits):
    return "".join(str(b) for b in bits)

def initial_permutation(bits):
    return [bits[i-1] for i in IP_TABLE]

if __name__=="__main__":
    sample_hex="0123456789ABCDEF"
    bits=str_to_bits(sample_hex,True)
    ip=initial_permutation(bits)
    print(bits_to_hex(ip))
    
    sample_ascii="ABCDEFGH"
    bits=str_to_bits(sample_ascii)
    ip=initial_permutation(bits)
    print(bits_to_hex(ip))
