from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

"""RSA is named for the MIT scientists 
(Rivest, Shamir, and Adleman). It is an asymmetric 
algorithm that uses a publicly known key for 
encryption, but requires a different key, known 
only to the intended recipient, for decryption."""

#Generate a public and private key
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

#Save public and private key (optional)
with open('private_key.pem','wb') as f: #wb: write on binary mode 
    f.write(private_key)
with open('public_key.pem','wb') as f:
    f.write(public_key)

#Encrypt data with public key
data = b"Crypto message RSA."
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
cipherData = cipher.encrypt(data)

#Decrypt data with private key
cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decryptedData = cipher.decrypt(cipherData)

print("Encrypted data: ", cipherData)
print("Decrypted data: ", decryptedData)