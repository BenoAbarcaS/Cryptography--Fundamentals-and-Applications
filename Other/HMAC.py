# HMAC (Hash-based Message Authentication Code) is a mechanism for verifying the integrity and authenticity of a message using a hash function and a secret key.

from Crypto.Hash import HMAC, SHA256

# Generate a secret key (in practice, this should be securely stored)
secret_key = b"my_secret_key"

# Create an HMAC object
hmac = HMAC.new(secret_key, digestmod=SHA256)

# Data to authenticate
data = b"Authenticate this message."

# Generate the HMAC
hmac.update(data)
mac = hmac.digest()

print("HMAC: ", mac)

# Verify the HMAC
hmac = HMAC.new(secret_key, digestmod=SHA256)
hmac.update(data)
try:
    hmac.verify(mac)
    print("The HMAC is valid.")
except ValueError:
    print("The HMAC is not valid.")