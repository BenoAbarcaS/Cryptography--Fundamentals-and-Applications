#CBC (Cipher Block Chaining) mode is a block cipher mode of operation 
#that uses a block of data to encrypt or decrypt data. 
#The block of data is called the initialization vector (IV).
#More secure than ECB mode, evade repetitive use of the same key.

#Does not provide data authentication
#Requires a unique initialization vector

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#Generate a random key 16 bytes and IV (initialization vector) 16 bytes
key = get_random_bytes(16)
iv = get_random_bytes(16)

#Create a object of AES on CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

#Data to encrypt
data = b"Crypto message AES CBC."

#Encrypt data
cipherData = cipher.encrypt(pad(data, AES.block_size))
print("Encrypted data: ", cipherData)

#Decrypt data
cipher = AES.new(key, AES.MODE_CBC, iv)
decryptedData = unpad(cipher.decrypt(cipherData), AES.block_size)
print("Decrypted data: ", decryptedData)
