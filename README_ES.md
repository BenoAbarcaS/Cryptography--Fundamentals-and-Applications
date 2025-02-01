# Criptografía: Fundamentos y Aplicaciones

Este repositorio proporciona conceptos y ejemplos prácticos para entender un sistema de seguridad completo, combinando cifrado simétrico (AES), cifrado asimétrico (RSA), modos de operación (CBC, GCM) y firmas digitales.

---

## **Idiomas Disponibles**

- [Inglés](README.md) (predeterminado)
- [Español](README_ES.md)

---

## **Tabla de Contenidos**

1. [Cifrado Simétrico (AES)](#1-cifrado-simétrico-aes)
2. [Cifrado Asimétrico (RSA)](#2-cifrado-asimétrico-rsa)
3. [Firmas Digitales](#3-firmas-digitales)
4. [Relación Entre Cifrado y Firmas Digitales](#4-relación-entre-cifrado-y-firmas-digitales)
5. [Otros Algoritmos Criptográficos](#5-otros-algoritmos-criptográficos)
6. [Combinaciones Comunes](#6-combinaciones-comunes)
7. [Recursos Adicionales](#7-recursos-adicionales)
8. [Ruta de Aprendizaje en Ciberseguridad](#8-ruta-de-aprendizaje-en-ciberseguridad)
9. [Licencia](#9-licencia)

---

## **1. Cifrado Simétrico (AES)**

### **¿Qué es AES?**

AES (**Advanced Encryption Standard**) es un algoritmo de cifrado simétrico, lo que significa que utiliza la misma clave para cifrar y descifrar datos. Es rápido y eficiente, ideal para cifrar grandes cantidades de datos.

### **Modos de Operación**

1. **ECB (Electronic Codebook)**:
   - Cada bloque se cifra de manera independiente.
   - **Problema**: Patrones repetitivos en los datos cifrados.
   - **Uso**: No recomendado para datos sensibles.
   - [Ver Explicación y Código ECB.py](./Symmetric/ECB.py)

2. **CBC (Cipher Block Chaining)**:
   - Cada bloque se cifra en función del bloque anterior.
   - Requiere un **IV (Vector de Inicialización)** para añadir aleatoriedad.
   - **Ventaja**: Más seguro que ECB.
   - [Ver Explicación y Código CBC.py](./Symmetric/CBC.py)

3. **GCM (Galois/Counter Mode)**:
   - Combina cifrado y autenticación.
   - Genera un **tag** que permite verificar la integridad de los datos.
   - **Ventaja**: Eficiente y seguro.
   - [Ver Explicación y Código GCM.py](./Symmetric/GCM.py)

---

## **2. Cifrado Asimétrico (RSA)**

### **¿Qué es RSA?**

RSA es un algoritmo de cifrado asimétrico, lo que significa que utiliza un par de claves: una **clave pública** (para cifrar) y una **clave privada** (para descifrar). Es más lento que el cifrado simétrico, pero ideal para tareas específicas como el intercambio de claves y las firmas digitales.

### **Características Clave**

- **Tamaños de clave**: 1024, 2048 o 4096 bits (se recomienda 2048 o superior).
- **Aplicaciones**:
  - Intercambio seguro de claves.
  - Firmas digitales.
- [Ver Explicación y Código RSA.py](./Asymmetric/RSA.py)

---

## **3. Firmas Digitales**

### **¿Qué es una Firma Digital?**

Una firma digital es un mecanismo criptográfico que permite:

1. **Autenticidad**: Verificar que el mensaje fue enviado por el remitente.
2. **Integridad**: Asegurar que el mensaje no ha sido modificado.
3. **No repudio**: El remitente no puede negar haber enviado el mensaje.

### **Cómo Funciona**

1. **Generación de claves**: Se genera un par de claves (pública y privada) utilizando un algoritmo como RSA o ECDSA.
2. **Firma**:
   - El remitente calcula el hash del mensaje.
   - El hash se cifra con la clave privada para generar la firma.
3. **Verificación**:
   - El receptor calcula el hash del mensaje recibido.
   - Utiliza la clave pública para descifrar la firma y compararla con el hash calculado.
   - Si coinciden, la firma es válida.

### **Ejemplo (RSA)**

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

## **4. Relación Entre Cifrado y Firmas Digitales**

### **Cifrado Simétrico (AES)**

- **Propósito**: Proteger la **confidencialidad** de los datos.
- **Uso**: Cifrado de archivos, comunicaciones seguras.

### **Cifrado Asimétrico (RSA)**

- **Propósito**: Facilitar el **intercambio seguro de claves** y las **firmas digitales**.
- **Uso**: Intercambio de claves, autenticación, integridad.

### **Combinación**

- **AES + RSA**: Usar RSA para intercambiar de manera segura una clave AES, luego usar AES para cifrar los datos.
- **Firmas digitales**: Usar RSA para firmar el hash de los datos cifrados con AES.

---

## **5. Otros Algoritmos Criptográficos**

### **ECDSA (Elliptic Curve Digital Signature Algorithm)**

#### **¿Qué es ECDSA?**

ECDSA es un algoritmo de firma digital basado en criptografía de curva elíptica. Es más eficiente que RSA y se utiliza ampliamente en aplicaciones como Bitcoin y Ethereum.

#### **Características Clave**

- **Eficiencia**: Requiere tamaños de clave más pequeños en comparación con RSA para el mismo nivel de seguridad.
- **Seguridad**: Basado en la complejidad matemática de las curvas elípticas.
- **Aplicaciones**: Firmas digitales, tecnología blockchain.

#### **Ver Código**

- [Ver Explicación y Código ECDSA.py](./other/ECDSA.py)

---

### **HMAC (Hash-based Message Authentication Code)**

#### **¿Qué es HMAC?**

HMAC es un mecanismo para verificar la integridad y autenticidad de un mensaje utilizando una función hash y una clave secreta.

#### **Características Clave**

- **Integridad**: Asegura que el mensaje no ha sido alterado.
- **Autenticación**: Verifica el remitente utilizando una clave secreta compartida.
- **Aplicaciones**: Comunicación segura, autenticación de API.

#### **Ver Código**

- [Ver Explicación y Código HMAC.py](./other/HMAC.py)

---

### **SHA-256 (Secure Hash Algorithm 256-bit)**

#### **¿Qué es SHA-256?**

SHA-256 es una función hash criptográfica ampliamente utilizada que produce un valor hash de 256 bits (32 bytes). Es parte de la familia de funciones hash SHA-2.

#### **Características Clave**

- **Salida Fija**: Siempre produce un hash de 256 bits.
- **Función Unidireccional**: Es computacionalmente inviable revertir el hash.
- **Aplicaciones**: Integridad de datos, blockchain, hashing de contraseñas.

#### **Ver Código**

- [Ver Explicación y Código SHA256.py](./other/SHA256.py)

---

## **6. Combinaciones Comunes**

### **AES + RSA**

#### **¿Qué es AES + RSA?**

Esta combinación utiliza RSA para intercambiar de manera segura una clave AES, y luego AES se utiliza para cifrar los datos. RSA proporciona un intercambio seguro de claves, mientras que AES asegura un cifrado eficiente de grandes cantidades de datos.

#### **Características Clave**

- **Intercambio Seguro de Claves**: RSA asegura que la clave AES se transmita de manera segura.
- **Cifrado Eficiente**: AES es rápido y eficiente para cifrar datos.
- **Aplicaciones**: Comunicación segura, cifrado de archivos.

#### **Ver Código**

- [Ver Explicación y Código AES_RSA.py](./combinations/AES_RSA.py)

---

### **HMAC + AES**

#### **¿Qué es HMAC + AES?**

Esta combinación utiliza HMAC para autenticar datos cifrados con AES. HMAC asegura la integridad y autenticidad de los datos cifrados.

#### **Características Clave**

- **Integridad de Datos**: HMAC verifica que los datos no han sido alterados.
- **Autenticación**: Asegura que los datos provienen de una fuente confiable.
- **Aplicaciones**: Comunicación segura, almacenamiento de datos.

#### **Ver Código**

- [Ver Explicación y Código HMAC_AES.py](./combinations/HMAC_AES.py)

---

## **7. Recursos Adicionales**

- [Documentación de PyCryptodome](https://pycryptodome.readthedocs.io/): Para profundizar en las funciones criptográficas.
- [Tutorial de RSA en Python](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/): Para entender mejor el algoritmo RSA.
- [Guía de Modos de Operación de AES](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation): Explicación detallada de CBC, GCM y otros modos.

---

## **8. Ruta de Aprendizaje en Ciberseguridad**

Este repositorio es parte de una serie de proyectos para aprender ciberseguridad. Aquí está el orden recomendado:

1. **[Criptografía: Fundamentos y Aplicaciones](https://github.com/BenoAbarcaS/Cryptography--Fundamentals-and-Applications)**

---

## **9. Licencia**

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.