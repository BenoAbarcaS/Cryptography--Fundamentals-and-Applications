# This combination uses RSA to securely exchange an AES key, and then AES is used to encrypt the data.

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA keys
rsa_key = RSA.generate(2048)
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

# Generate a random AES key
aes_key = get_random_bytes(16)

# Encrypt the AES key with RSA
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

# Encrypt data with AES
data = b"Secret message to encrypt."
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

# Decrypt the AES key with RSA
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted_aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Decrypt data with AES
cipher_aes = AES.new(decrypted_aes_key, AES.MODE_EAX, cipher_aes.nonce)
decrypted_data = cipher_aes.decrypt_and_verify(ciphertext, tag)

print("Decrypted data: ", decrypted_data)