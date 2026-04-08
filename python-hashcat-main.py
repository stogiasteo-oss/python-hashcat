import hashlib

target_hash = input("Paste your MD5 hashed 32 character password here:")
# md5 για "password"
while 

with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        word = line.strip()
        hashed = hashlib.md5(word.encode()).hexdigest()
        
        if hashed == target_hash:
            print("Found:", word)
            break
