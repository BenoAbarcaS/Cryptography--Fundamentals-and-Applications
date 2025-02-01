# Cryptography: Fundamentals and Applications

This repository aims to provide the concepts and practical examples to understand a complete security system, combining symmetric encryption (AES), asymmetric encryption (RSA), modes of operation (CBC, GCM), and digital signatures.

---

## **Available Languages**

- [English](README.md) (default)
- [Español](README_ES.md)

---

## **1. Symmetric Encryption (AES)**

### **What is AES?**

AES (**Advanced Encryption Standard**) is a symmetric encryption algorithm, meaning it uses the same key to encrypt and decrypt data. It is fast and efficient, ideal for encrypting large amounts of data.

### **Modes of Operation**

1. **ECB (Electronic Codebook)**:
   - Each block is encrypted independently.
   - **Issue**: Repetitive patterns in the encrypted data.
   - **Use**: Not recommended for sensitive data.
   - [View code ECB.py](./Symmetric/ECB.py)

2. **CBC (Cipher Block Chaining)**:
   - Each block is encrypted based on the previous block.
   - Requires an **IV (Initialization Vector)** to add randomness.
   - **Advantage**: More secure than ECB.
   - [View code CBC.py](./Symmetric/CBC.py)

3. **GCM (Galois/Counter Mode)**:
   - Combines encryption and authentication.
   - Generates a **tag** that allows verifying data integrity.
   - **Advantage**: Efficient and secure.
   - [View code GCM.py](./Symmetric/GCM.py)

---

## **2. Asymmetric Encryption (RSA)**

### **What is RSA?**

RSA is an asymmetric encryption algorithm, meaning it uses a pair of keys: a **public key** (to encrypt) and a **private key** (to decrypt). It is slower than symmetric encryption but ideal for specific tasks like key exchange and digital signatures.

### **Key Features**

- **Key sizes**: 1024, 2048, or 4096 bits (recommended 2048 or higher).
- **Applications**:
  - Secure key exchange.
  - Digital signatures.
- [View code RSA.py](./Asymmetric/RSA.py)

---

## **3. Digital Signatures**

### **What is a Digital Signature?**

A digital signature is a cryptographic mechanism that allows:

1. **Authenticity**: Verify that the message was sent by the sender.
2. **Integrity**: Ensure that the message has not been modified.
3. **Non-repudiation**: The sender cannot deny sending the message.

### **How It Works**

1. **Key generation**: A key pair (public and private) is generated using an algorithm like RSA or ECDSA.
2. **Signing**:
   - The sender calculates the hash of the message.
   - The hash is encrypted with the private key to generate the signature.
3. **Verification**:
   - The receiver calculates the hash of the received message.
   - Uses the public key to decrypt the signature and compare it with the calculated hash.
   - If they match, the signature is valid.

### **Example (RSA)**

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generar claves
clave = RSA.generate(2048)
clave_privada = clave.export_key()
clave_publica = clave.publickey().export_key()

# Firmar un mensaje
mensaje = b"Este es un mensaje importante."
hash_mensaje = SHA256.new(mensaje)
firma = pkcs1_15.new(RSA.import_key(clave_privada)).sign(hash_mensaje)

# Verificar la firma
try:
    pkcs1_15.new(RSA.import_key(clave_publica)).verify(hash_mensaje, firma)
    print("La firma es válida.")
except (ValueError, TypeError):
    print("La firma no es válida.")
```

---

## **4. Relationship Between Encryption and Digital Signatures**

### **Symmetric Encryption (AES)**

- **Purpose**: Protect the **confidentiality** of data.
- **Use**: File encryption, secure communications.

### **Asymmetric Encryption (RSA)**

- **Purpose**: Facilitate **secure key exchange** and **digital signatures**.
- **Use**: Key exchange, authentication, integrity.

### **Combination**

- **AES + RSA**: Use RSA to securely exchange an AES key, then use AES to encrypt the data.
- **Digital signatures**: Use RSA to sign the hash of the data encrypted with AES.

---

## **5. Additional Resources**

- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/): To dive deeper into cryptographic functions.
- [RSA Tutorial in Python](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/): To better understand the RSA algorithm.
- [AES Modes of Operation Guide](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation): Detailed explanation of CBC, GCM, and other modes.

---

## **Cybersecurity Learning Path**

This repository is part of a series of projects to learn cybersecurity. Here is the recommended order:

1. **[Cryptography: Fundamentals and Applications](https://github.com/BenoAbarcaS/Cryptography--Fundamentals-and-Applications)**
