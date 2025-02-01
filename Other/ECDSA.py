# ECDSA (Elliptic Curve Digital Signature Algorithm) is a digital signature algorithm based on elliptic curve cryptography.
# It is more efficient than RSA and is widely used in applications like Bitcoin and Ethereum.

from Crypto.PublicKey import ECC  # Import ECC for elliptic curve cryptography
from Crypto.Signature import DSS  # Import DSS for digital signatures
from Crypto.Hash import SHA256    # Import SHA256 for hashing

# Generate an ECC key pair
# ECC keys are generated using a specific elliptic curve (e.g., 'P-256').
key = ECC.generate(curve='P-256')

# Export the private key in PEM format
private_key = key.export_key(format='PEM')

# Export the public key in PEM format
public_key = key.public_key().export_key(format='PEM')

# Save the private key to a file (optional)
with open('private_key.pem', 'w') as f:
    f.write(private_key)

# Save the public key to a file (optional)
with open('public_key.pem', 'w') as f:
    f.write(public_key)

# Sign a message
message = b"This is an important message."  # Message to sign
message_hash = SHA256.new(message)         # Hash the message using SHA-256
signer = DSS.new(key, 'fips-186-3')        # Create a signer object using the private key
signature = signer.sign(message_hash)      # Generate the signature

print("Signature: ", signature)

# Verify the signature
verifier = DSS.new(ECC.import_key(public_key), 'fips-186-3')  # Create a verifier object using the public key
try:
    verifier.verify(message_hash, signature)  # Verify the signature
    print("The signature is valid.")          # If valid, print success message
except ValueError:
    print("The signature is not valid.")      # If invalid, print error message