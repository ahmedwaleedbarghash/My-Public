from cryptography.fernet import Fernet

# Initialize new key every time we use this code
secret_key = Fernet.generate_key()
# We generated a new key stored in mykey.key file
with open('Fernet_crypto/write-upkey.key', 'wb') as mykey:
    key = mykey.write(secret_key)
