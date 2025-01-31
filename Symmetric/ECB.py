from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

"""AES (Advanced Encryption Standard) is a symmetric block cipher,
which means that the same key is used to encrypt and decrypt the data."""

#Generate a random key 16 bytes 
key = get_random_bytes(16)

#Create a object of AES on ECB mode (electronic codebook)
cipher = AES.new(key, AES.MODE_ECB)

#Data to encrypt
data = b"Crypto message AES ECB."

#Encrypt data
cipherData = cipher.encrypt(pad(data, AES.block_size))
print("Encrypted data: ", cipherData)

#Decrypt data
decryptedData = unpad(cipher.decrypt(cipherData), AES.block_size)
print("Decrypted data: ", decryptedData)

"""This code is for test, you can use a random key, create a Object of AES on CBC mode.
AES requires data to be a multiple of 16 bytes, pad and unpad data used for this"""