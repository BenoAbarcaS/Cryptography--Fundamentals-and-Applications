# Criptografía: Fundamentos y Aplicaciones

Este repositorio tiene como objetivo proporcionar los conceptos y ejemplos prácticos para entender un sistema de seguridad completo, combinando cifrado simétrico (AES), cifrado asimétrico (RSA), modos de operación (CBC, GCM) y firmas digitales.

---

## **Idiomas Disponibles**

- [English](README.md) (predeterminado)
- [Español](README_ES.md)

---

## **1. Cifrado Simétrico (AES)**

### **¿Qué es AES?**

AES (**Advanced Encryption Standard**) es un algoritmo de cifrado simétrico, lo que significa que usa la misma clave para cifrar y descifrar datos. Es rápido y eficiente, ideal para cifrar grandes cantidades de datos.

### **Modos de Operación**

1. **ECB (Electronic Codebook)**:
   - Cada bloque se cifra de manera independiente.
   - **Problema**: Patrones repetitivos en los datos cifrados.
   - **Uso**: No recomendado para datos sensibles.
   - [Ver código ECB.py](./Symmetric/ECB.py)

2. **CBC (Cipher Block Chaining)**:
   - Cada bloque se cifra en función del bloque anterior.
   - Requiere un **IV (Initialization Vector)** para añadir aleatoriedad.
   - **Ventaja**: Mayor seguridad que ECB.
   - [Ver código CBC.py](./Symmetric/CBC.py)

3. **GCM (Galois/Counter Mode)**:
   - Combina cifrado y autenticación.
   - Genera un **tag** que permite verificar la integridad de los datos.
   - **Ventaja**: Eficiente y seguro.
   - [Ver código GCM.py](./Symmetric/GCM.py)

---

## **2. Cifrado Asimétrico (RSA)**

### **¿Qué es RSA?**

RSA es un algoritmo de cifrado asimétrico, lo que significa que usa un par de claves: una **clave pública** (para cifrar) y una **clave privada** (para descifrar). Es más lento que el cifrado simétrico, pero es ideal para tareas específicas como el intercambio de claves y las firmas digitales.

### **Características**

- **Tamaños de clave**: 1024, 2048 o 4096 bits (recomendado 2048 o superior).
- **Aplicaciones**:
  - Intercambio seguro de claves.
  - Firmas digitales.
- [Ver código RSA.py](./Asymmetric/RSA.py)

---

## **3. Firmas Digitales**

### **¿Qué es una firma digital?**

Una firma digital es un mecanismo criptográfico que permite:

1. **Autenticidad**: Verificar que el mensaje fue enviado por el remitente.
2. **Integridad**: Asegurar que el mensaje no ha sido modificado.
3. **No repudio**: El remitente no puede negar que envió el mensaje.

### **Funcionamiento**

1. **Generación de claves**: Se genera un par de claves (pública y privada) usando un algoritmo como RSA o ECDSA.
2. **Firma**:
   - El remitente calcula el hash del mensaje.
   - El hash se cifra con la clave privada para generar la firma.
3. **Verificación**:
   - El receptor calcula el hash del mensaje recibido.
   - Usa la clave pública para descifrar la firma y compararla con el hash calculado.
   - Si coinciden, la firma es válida.

### **Ejemplo (RSA)**

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

## **4. Relación entre Cifrado y Firmas Digitales**

### **Cifrado Simétrico (AES)**

- **Propósito**: Proteger la **confidencialidad** de los datos.
- **Uso**: Cifrado de archivos, comunicaciones seguras.

### **Cifrado Asimétrico (RSA)**

- **Propósito**: Facilitar el **intercambio seguro de claves** y las **firmas digitales**.
- **Uso**: Intercambio de claves, autenticación, integridad.

### **Combinación**

- **AES + RSA**: Usa RSA para intercambiar una clave AES de manera segura, y luego usa AES para cifrar los datos.
- **Firmas digitales**: Usa RSA para firmar el hash de los datos cifrados con AES.

---

## **5. Recursos Adicionales**

- [Documentación de PyCryptodome](https://pycryptodome.readthedocs.io/): Para profundizar en las funciones de criptografía.
- [Tutorial de RSA en Python](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/): Para entender mejor el algoritmo RSA.
- [Guía de modos de operación AES](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation): Explicación detallada de CBC, GCM y otros modos.

---

## **Ruta de Aprendizaje en Ciberseguridad**

Este repositorio es parte de una serie de proyectos para aprender ciberseguridad. Aquí tienes el orden recomendado:

1. **[Criptografía: Fundamentos y Aplicaciones](https://github.com/BenoAbarcaS/Cryptography--Fundamentals-and-Applications)**

---

## **Licencia**

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
