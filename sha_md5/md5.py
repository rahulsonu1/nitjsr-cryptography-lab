import hashlib

def generate_md5(message: str) -> str:
   
    md5_hash = hashlib.md5(message.encode())
    return md5_hash.hexdigest()


if __name__ == "__main__":
    message = "hello world"
    md5_result = generate_md5(message)
    print("MD5 Hash:", md5_result)