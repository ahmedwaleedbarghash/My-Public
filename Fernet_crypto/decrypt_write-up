## Introduction

In today's digital world, securing data is of utmost importance. One effective way to protect sensitive information is through encryption. Symmetric encryption, where the same key is used for both encryption and decryption, is a widely used method. This write-up explains how to implement symmetric encryption using the `Fernet` module from the `cryptography` library in Python.

## Overview of the Process

This process involves the following key steps:

1. **Key Generation**: A secret key is generated and stored for future use.
2. **Encryption**: The data is encrypted using the generated key.
3. **Decryption**: The encrypted data can be decrypted back to its original form using the same key.

## Implementation Steps

### 1. Importing Required Libraries

First, we need to import the `Fernet` class from the `cryptography.fernet` module:

python

Copy

```
from cryptography.fernet import Fernet
```

### 2. Key Generation

A secret key is generated for encryption purposes. This key must be securely stored, as it is required for both encrypting and decrypting data.

python

Copy

```
# Generate a new key
secret_key = Fernet.generate_key()

# Store the key in a file
with open('Fernet_crypto/mykey.key', 'wb') as mykey:
    mykey.write(secret_key)
```

### 3. Encrypting Data

With the key generated, we can proceed to encrypt the data. This involves reading the original data from a file, encrypting it using the `Fernet` object initialized with our key, and then writing the encrypted data to a new file.

python

Copy

```
# Read the key from the file
with open('Fernet_crypto/mykey.key', 'rb') as mykey:
    skey = mykey.read()

# Initialize the Fernet object with the key
f = Fernet(skey)

# Read the original data
with open('Fernet_crypto/text.txt', 'rb') as original_file:
    original = original_file.read()

# Encrypt the data
encrypted = f.encrypt(original)

# Write the encrypted data to a new file
with open('Fernet_crypto/enc_text', 'wb') as enc_file:
    enc_file.write(encrypted)
```

### 4. Decrypting Data

To retrieve the original data, we need to decrypt the encrypted file using the same key. This process involves reading the encrypted data, decrypting it, and writing the decrypted data to a new file.

python

Copy

```
# Read the encrypted file
with open('Fernet_crypto/enc_text', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

# Decrypt the data
decrypted = f.decrypt(encrypted)

# Write the decrypted data to a new file
with open('Fernet_crypto/after_dec', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
```

## Conclusion

Using the `cryptography` library's `Fernet` module, we can effectively secure data through symmetric encryption. This implementation illustrates how to generate a key, encrypt data, and decrypt it back to its original form. Proper management of the encryption key is crucial to maintaining the confidentiality of the data.

By following these steps, you can ensure that sensitive information is securely encrypted and can only be accessed by those who possess the correct key.