# This combination uses HMAC to authenticate data encrypted with AES.

from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

# Generate a random AES key and HMAC key
aes_key = get_random_bytes(16)
hmac_key = get_random_bytes(16)

# Encrypt data with AES
data = b"Secret message to encrypt."
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

# Generate HMAC for the ciphertext
hmac = HMAC.new(hmac_key, digestmod=SHA256)
hmac.update(ciphertext)
mac = hmac.digest()

# Verify HMAC and decrypt data
hmac = HMAC.new(hmac_key, digestmod=SHA256)
hmac.update(ciphertext)
try:
    hmac.verify(mac)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, cipher_aes.nonce)
    decrypted_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print("Decrypted data: ", decrypted_data)
except ValueError:
    print("HMAC verification failed.")