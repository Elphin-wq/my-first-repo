from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
#Encryption
key=get_random_bytes(16) # AES key must be either 16, 24 or 32 bytes
cipher=AES.new(key,AES.MODE_EAX)
nonce=cipher.nonce
mymessage=input("Enter Your Message:")
message_bytes=mymessage.encode("utf-8")
ciphertext,tag=cipher.encrypt_and_digest(message_bytes)
print(ciphertext)
#Decrypt
cipher=AES.new(key,AES.MODE_EAX,nonce=nonce)
plaintext=cipher.decrypt_and_verify(ciphertext,tag)
print(plaintext.decode()) # should print secret message