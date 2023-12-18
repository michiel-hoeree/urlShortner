import hashlib


def bereken_hash(data):
    hash = hashlib.sha256(data.encode())
    return hash.hexdigest()



test = "test"
hash1 = bereken_hash(test)
hash2 = bereken_hash(hash1)
hash3 = bereken_hash(hash2)
hash4 = bereken_hash(hash3)
hash5 = bereken_hash(hash4)
print(test)
print(hash1)
print(hash2)
print(hash3)
print(hash4)
print(hash5)