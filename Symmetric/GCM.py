#Galois/Counter Mode (GCM) is a mode of operation that combines encryption and authentication.
#Provides confidentiality (encryption) and integrity (authentication) of the data
#It generates a tag to verify that the data has not been modified.

#Counter mode encryption: Data is encrypted using a unique counter.
#Authentication: A tag is calculated using an authentication algorithm based on multiplication in the Galois field.
#Verification: When decrypting, the tag is verified to ensure data integrity.
#Requires a nonce (unique number) for each encryption operation.

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Generate a random key 16 bytes and nonce 12 bytes
key = get_random_bytes(16)
nonce = get_random_bytes(12)

#Create a object of AES on GCM mode
cipher = AES.new(key, AES.MODE_GCM, nonce)

#Data to encrypt
data = b"Crypto message AES GCM."

#Encrypt data
cipherData, tag = cipher.encrypt_and_digest(data)
print("Encrypted data: ", cipherData)
print("Tag: ", tag)

#Decrypt data
cipher = AES.new(key, AES.MODE_GCM, nonce)
decryptedData = cipher.decrypt(cipherData)
print("Decrypted data: ", decryptedData)

