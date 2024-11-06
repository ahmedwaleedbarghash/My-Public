# First we have to import fernet which is symmetric encryption
from cryptography.fernet import Fernet 

# Then we have to read the mykey.key file in the local storage
with open('Fernet_crypto/write-upkey.key', 'rb') as mykey:
    skey = mykey.read()

# # Print the key for checking if it the same key we initialized
# print(skey)


# Then we will initialize variable which is takes the key as an argument
f = Fernet(skey)

# The next step we will read our file and stored as original
with open('Fernet_crypto/Symmetric Encryption with Fernet.md', 'rb') as original_file:
    original = original_file.read()


# Now we can encrypt the file using Fernet object that has our key -> 'f' and store it as encrypted
encrypted = f.encrypt(original)

# Finally we will write the encrypted data in new file
with open('Fernet_crypto/enc_write-up', 'wb') as enc_file:
    enc_file.write(encrypted)
