def ceaserCipherEncryption(s,k):
    ans=""
    for i in range(0,len(s)):
        char =s[i]
        if(char.isupper()):
            ans=ans+chr((ord(char)+k-65)%26+65)
        else:
            ans=ans+chr((ord(char)+k-97)%26+97)
    return ans
    
def ceaserCipherDecryption(s,k):
    ans=""
    for i in range(0,len(s)):
        char =s[i]
        if(char.isupper()):
            ans=ans+chr((ord(char)-k-65)%26+65)
        else:
            ans=ans+chr((ord(char)-k-97)%26+97)
    return ans



s="PDAKLANWPEKJOPWNP"
for i in range(0,25):
    print(i)
    decrypted=ceaserCipherDecryption(s,i)
    print(decrypted)

