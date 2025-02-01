# SHA-256 (Secure Hash Algorithm 256-bit) is a widely used cryptographic hash function that produces a 256-bit (32-byte) hash value.

from Crypto.Hash import SHA256

# Data to hash
data = b"Hash this message."

# Create a SHA-256 hash object
hash_object = SHA256.new(data)

# Get the hash value
hash_value = hash_object.digest()

print("SHA-256 Hash: ", hash_value)