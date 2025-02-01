# Cryptography: Fundamentals and Applications

This repository provides concepts and practical examples to understand a complete security system, combining symmetric encryption (AES), asymmetric encryption (RSA), modes of operation (CBC, GCM), and digital signatures.

---

## **Available Languages**

- [English](README.md) (default)
- [Español](README_ES.md)

---

## **Table of Contents**

1. [Symmetric Encryption (AES)](#1-symmetric-encryption-aes)
2. [Asymmetric Encryption (RSA)](#2-asymmetric-encryption-rsa)
3. [Digital Signatures](#3-digital-signatures)
4. [Relationship Between Encryption and Digital Signatures](#4-relationship-between-encryption-and-digital-signatures)
5. [Other Cryptographic Algorithms](#5-other-cryptographic-algorithms)
6. [Common Combinations](#6-common-combinations)
7. [Additional Resources](#7-additional-resources)
8. [Cybersecurity Learning Path](#8-cybersecurity-learning-path)
9. [License](#9-license)

---

## **0. Practical Examples**

All the practical examples to see will be available in the repository as well as in a single **Google Collab** file. You can access them through **[this link](https://colab.research.google.com/drive/1YcJKbu3w18cmb7xH8x0DhmLPBQudPtY9?usp=sharing)**.

---

## **1. Symmetric Encryption (AES)**

### **What is AES?**

AES (**Advanced Encryption Standard**) is a symmetric encryption algorithm, meaning it uses the same key to encrypt and decrypt data. It is fast and efficient, ideal for encrypting large amounts of data.

### **Modes of Operation**

1. **ECB (Electronic Codebook)**:
   - Each block is encrypted independently.
   - **Issue**: Repetitive patterns in the encrypted data.
   - **Use**: Not recommended for sensitive data.
   - [View Explaination and Code ECB.py](./Symmetric/ECB.py)

2. **CBC (Cipher Block Chaining)**:
   - Each block is encrypted based on the previous block.
   - Requires an **IV (Initialization Vector)** to add randomness.
   - **Advantage**: More secure than ECB.
   - [View Explaination and code CBC.py](./Symmetric/CBC.py)

3. **GCM (Galois/Counter Mode)**:
   - Combines encryption and authentication.
   - Generates a **tag** that allows verifying data integrity.
   - **Advantage**: Efficient and secure.
   - [View Explaination and code GCM.py](./Symmetric/GCM.py)

---

## **2. Asymmetric Encryption (RSA)**

### **What is RSA?**

RSA is an asymmetric encryption algorithm, meaning it uses a pair of keys: a **public key** (to encrypt) and a **private key** (to decrypt). It is slower than symmetric encryption but ideal for specific tasks like key exchange and digital signatures.

### **Key Features**

- **Key sizes**: 1024, 2048, or 4096 bits (recommended 2048 or higher).
- **Applications**:
  - Secure key exchange.
  - Digital signatures.
- [View Explaination and code RSA.py](./Asymmetric/RSA.py)

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

# Generate keys
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Sign a message
message = b"This is an important message."
message_hash = SHA256.new(message)
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(message_hash)

# Verify the signature
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(message_hash, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is not valid.")
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

## **5. Other Cryptographic Algorithms**

### **ECDSA (Elliptic Curve Digital Signature Algorithm)**

#### **What is ECDSA?**

ECDSA is a digital signature algorithm based on elliptic curve cryptography. It is more efficient than RSA and is widely used in applications like Bitcoin and Ethereum.

#### **Key Features**

- **Efficiency**: Requires smaller key sizes compared to RSA for the same level of security.
- **Security**: Based on the mathematical complexity of elliptic curves.
- **Applications**: Digital signatures, blockchain technology.

#### **View Code**

- [View Explaination and code ECDSA.py](./other/ECDSA.py)

---

### **HMAC (Hash-based Message Authentication Code)**

#### **What is HMAC?**

HMAC is a mechanism for verifying the integrity and authenticity of a message using a hash function and a secret key.

#### **Key Features**

- **Integrity**: Ensures that the message has not been tampered with.
- **Authentication**: Verifies the sender using a shared secret key.
- **Applications**: Secure communication, API authentication.

#### **View Code**

- [View Explaination and code HMAC.py](./other/HMAC.py)

---

### **SHA-256 (Secure Hash Algorithm 256-bit)**

#### **What is SHA-256?**

SHA-256 is a widely used cryptographic hash function that produces a 256-bit (32-byte) hash value. It is part of the SHA-2 family of hash functions.

#### **Key Features**

- **Fixed Output**: Always produces a 256-bit hash.
- **One-way Function**: It is computationally infeasible to reverse the hash.
- **Applications**: Data integrity, blockchain, password hashing.

#### **View Code**

- [View Explaination and code SHA256.py](./other/SHA256.py)

---

## **6. Common Combinations**

### **AES + RSA**

#### **What is AES + RSA?**

This combination uses RSA to securely exchange an AES key, and then AES is used to encrypt the data. RSA provides secure key exchange, while AES ensures efficient encryption of large amounts of data.

#### **Key Features**

- **Secure Key Exchange**: RSA ensures that the AES key is securely transmitted.
- **Efficient Encryption**: AES is fast and efficient for encrypting data.
- **Applications**: Secure communication, file encryption.

#### **View Code**

- [View Explaination and code AES_RSA.py](./combinations/AES_RSA.py)

---

### **HMAC + AES**

#### **What is HMAC + AES?**

This combination uses HMAC to authenticate data encrypted with AES. HMAC ensures the integrity and authenticity of the encrypted data.

#### **Key Features**

- **Data Integrity**: HMAC verifies that the data has not been tampered with.
- **Authentication**: Ensures that the data comes from a trusted source.
- **Applications**: Secure communication, data storage.

#### **View Code**

- [View Explaination and code HMAC_AES.py](./combinations/HMAC_AES.py)

---

## **7. Additional Resources**

- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/): To dive deeper into cryptographic functions.
- [RSA Tutorial in Python](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/): To better understand the RSA algorithm.
- [AES Modes of Operation Guide](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation): Detailed explanation of CBC, GCM, and other modes.

---

## **8. Cybersecurity Learning Path**

This repository is part of a series of projects to learn cybersecurity. Here is the recommended order:

1. **[Cryptography: Fundamentals and Applications](https://github.com/BenoAbarcaS/Cryptography--Fundamentals-and-Applications)**

---

## **9. License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
