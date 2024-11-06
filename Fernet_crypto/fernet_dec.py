# First we have to import fernet which is symmetric encryption
from cryptography.fernet import Fernet

# Then we have to read the mykey.key file in the local storage
with open('Fernet_crypto/write-upkey.key', 'rb') as mykey:
    k = mykey.read()

# # Print the key for checking if it the same key we initialized
# print(skey)

# Then we will initialize variable which is takes the key as an argument
f = Fernet(k)

# The next step we will read our file and stored as encrypted
with open('Fernet_crypto/enc_write-up', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

# Now we use fernet function to decrypt the encrypted file
decrypted = f.decrypt(encrypted)

# Finally we stored the decrypted data in new file
with open('Fernet_crypto/decrypt_write-up', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

    