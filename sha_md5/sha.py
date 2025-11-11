import hashlib

def sha_128(message):
    # Encode the message to bytes
    msg_bytes = message.encode('utf-8')
    
    # Create MD5 hash object (128-bit digest)
    hash_obj = hashlib.md5(msg_bytes)
    
    
    return hash_obj.hexdigest()

if __name__ == "__main__":
    message = input("Enter message: ")
    hash_value = sha_128(message)
    print("SHA-128 (MD5) Hash Value:")
    print(hash_value)