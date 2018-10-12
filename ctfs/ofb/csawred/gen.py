from Crypto.Cipher import DES
import binascii

key = open('key').read()
iv = '66642069'
cipher = DES.new(key, DES.MODE_OFB, iv)
plaintext = open('plain.txt').read()
msg = iv + cipher.encrypt(plaintext)
with open('destiny.enc', 'w') as f:
f.write(msg)
