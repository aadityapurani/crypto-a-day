from Crypto.Cipher import AES
import os
import sys
sys.path.insert(0,os.getcwd()+'/src')
import CBC_ECB_detction
import CBC_mode
import useful_functions
key = bytes(CBC_ECB_detction.randomKey(AES.block_size))
iv = bytearray(CBC_ECB_detction.randomKey(AES.block_size))

def encryption_oracle(input_data):
    input_data = input_data.replace(';','%3b').replace('=','%3d')
    plaintext = bytearray(
        "comment1=cooking%20MCs;userdata=" +
        input_data +
        ";comment2=%20like%20a%20pound%20of%20bacon"
    )
    return CBC_mode.aes_128_cbc_enc(plaintext, key, iv)

def is_admin(enc_data):
    plaintext = CBC_mode.aes_128_cbc_dec(enc_data, key, iv)
    return ";admin=true;" in plaintext
    
def crack():
    first_block = bytearray('A' * AES.block_size)
    second_block = bytearray("AadminAtrueA")
    plaintext = first_block + second_block
    ciphertext = encryption_oracle(plaintext)
    # We 'know' the prefix is two blocks long
    offset = 32
    # Change the first byte in first_block 'A' so we change the first byte in
    # second_block to be ';'
    ciphertext[offset] = bytes(
        useful_functions.xor(
            bytearray(chr(ciphertext[offset])),
            useful_functions.xor(bytearray("A"), bytearray(";"))
        )
    )
    # Change the 7th byte in first_block 'A' so we change the first byte in
    # second_block to be '='
    ciphertext[offset + 6] = bytes(
        useful_functions.xor(
            bytearray(chr(ciphertext[offset + 6])),
            useful_functions.xor(bytearray("A"), bytearray("="))
        )
    )
    # Change the 12th byte in first_block 'A' so we change the first byte in
    # second_block to be ';'
    ciphertext[offset + 11] = bytes(
        useful_functions.xor(
            bytearray(chr(ciphertext[offset + 11])),
            useful_functions.xor(bytearray("A"), bytearray(";"))
        )
    )
    return is_admin(ciphertext)