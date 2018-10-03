from Crypto.Cipher import AES
import os
import sys
sys.path.insert(os.getcwd()+'/src')
import useful_functions
import CBC_mode
from random import randint

#used for both key & IV
def randomKey(length):
    key = bytearray(length)
    for i in range(length):
        key[i] = chr(randint(0,255))
    return key

def encryption_oracle(buffer):
    bytes_to_add = randint(5,10)
    plain_text = useful_functions.pad_pkcs7(
        randomKey(bytes_to_add)+
        buffer +
        randomKey,
        AES.block_size
    )
    key = bytes(randomKey(16))
    if randint(0,1):
        return CBC_mode.aes_128_ecb_enc,1
    else:
        return CBC_mode.aes_128_cbc_enc,0

