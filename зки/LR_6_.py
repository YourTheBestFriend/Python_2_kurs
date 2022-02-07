from Crypto.Cipher import AES
import binascii

KEY = binascii.unhexlify('AAAABBBBCCCCDDDDEEEEFFFF00001111')

plaintext = binascii.unhexlify('11112222333344445555666677778888')
rijn = AES.new(KEY, AES.MODE_ECB)
ciphertext = rijn.encrypt(plaintext)
binascii.hexlify(ciphertext)
print(binascii.hexlify(ciphertext).decode('utf-8'))
