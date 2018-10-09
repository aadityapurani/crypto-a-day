import os
import sys
sys.path.insert(0,os.getcwd()+'/src')
import CBC_ECB_detction
import CBC_mode
import useful_functions
import padding_validation

import base64
from random import randint
from Crypto import Random
from Crypto.Cipher import AES

texts = [
    "MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
    "MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
    "MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
    "MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
    "MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
    "MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
    "MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
    "MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
    "MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
    "MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"
    ]

class Oracle:
    
    def __init__(self,possible_inputs):
        self.iv = Random.new().read(AES.block_size)
        self._key = Random.new().read(16)
        self._possible_inputs = possible_inputs
    
    def get_encryption_message(self):
        chosen_input = self._possible_inputs[randint(0,len(self._possible_inputs)-1)].encode()
        #chosen_input = chosen_input.encode()
        #print(type(chosen_input))
        return CBC_mode.aes_128_cbc_enc(bytearray(chosen_input),bytearray(self._key),bytearray(self.iv))
    
    def decrypt_and_check_padding(self,cipher_text,iv):
        #print("in dec\n")
        plain_text = CBC_mode.aes_128_cbc_dec(bytearray(cipher_text),bytearray(self._key),bytearray(self.iv))
        return useful_functions.is_pkcs7_padded(plain_text)
        '''
        plaintext = aes_cbc_decrypt(ciphertext, self._key, iv, False)
        return is_pkcs7_padded(plaintext)
        '''
'''
def create_forced_prev_block(iv,guessedByte,paddinglen,found_text):
    iv = bytearray(iv)
    #print(len(iv))
    found_text = bytearray(found_text)
    index_forced_byte = len(iv) - paddinglen
    #print(paddinglen)
    
    forced_char = iv[index_forced_byte] ^ guessedByte ^ paddinglen
    
    output = iv[:index_forced_byte] + bytes([forced_char])

    m = 0
    for k in range(AES.block_size - paddinglen+1, AES.block_size):
        forced_char = iv[k] ^ found_text[m] ^ paddinglen
        output += bytes([forced_char])
        m+=1
    return output

#try decoding the  first block
def attack_padding_oracle(cipher_text,oracle):
    plaintext = b''
    cipher_blocks = [oracle.iv] + [cipher_text[i:i+AES.block_size] for i in range(0,len(cipher_text),AES.block_size)]
    for c in range(1,len(cipher_blocks)):
        plaintext_block = b''
        #for each of the blocks
        print("each block")
        for i in range(AES.block_size-1,-1,-1):
            paddinglen = len(plaintext_block) + 1
            potential_last_bytes = []
            #for each of the potential bytes
            print("checking byte")
            for j in range(256):
                forced_iv = create_forced_prev_block(cipher_blocks[c-1],j,paddinglen,plaintext_block)
                #print("got forced")
                if(oracle.decrypt_and_check_padding(cipher_blocks[c],forced_iv) is True):
                    print("found something")
                    potential_last_bytes += [j]
                #print("finished byte")
            
            #double check for ambiguity

            if len(potential_last_bytes) != 1:
                for byte in potential_last_bytes:
                    for j in range(256):
                        forced_iv = create_forced_prev_block(cipher_blocks[c - 1], j, paddinglen + 1,
                                                                 bytes([byte]) + plaintext_block)

                        # If we manage to get a valid padding, then it's very likely that this
                        # candidate is the one that we want. So exclude the others and exit the loop.
                        if oracle.decrypt_and_check_padding(cipher_blocks[c], forced_iv) is True:
                            possible_last_bytes = [byte]
                            break
            if(len(potential_last_bytes)==0):
                print("found nothign")
            plaintext_block = bytes([potential_last_bytes[0]]) + plaintext_block
        plaintext += plaintext_block

    return padding_validation.unpad_valid_pkcs7(plaintext)
'''
def create_forced_previous_block(iv, guessed_byte, padding_len, found_plaintext):
    """Creates a forced block of the ciphertext, ideally to be given as IV to decrypt the following block.
    The forced IV will be used for the attack on the padding oracle CBC encryption.
    """

    # Get the index of the first character of the padding
    index_of_forced_char = len(iv) - padding_len
    iv = bytearray(iv)
    # Using the guessed byte given as input, try to force the first character of the
    # padding to be equal to the length of the padding itself
    forced_character = iv[index_of_forced_char] ^ guessed_byte ^ padding_len

    # Form the forced ciphertext by adding to it the forced character...
    output = iv[:index_of_forced_char] + bytes([forced_character])

    # ...and the characters that were forced before (for which we already know the plaintext)
    m = 0
    for k in range(AES.block_size - padding_len + 1, AES.block_size):

        # Force each of the following characters of the IV so that the matching characters in
        # the following block will be decrypted to "padding_len"
        forced_character = iv[k] ^ found_plaintext[m] ^ padding_len
        output += bytes([forced_character])
        m += 1

    return output


def attack_padding_oracle(ciphertext, oracle):
    """Decrypts the given ciphertext by using the padding oracle CBC encryption attack."""
    plaintext = b''

    # Split the ciphertext in blocks of the AES block_size (which can get it from the IV too)
    ciphertext_blocks = [oracle.iv] + [ciphertext[i:i + AES.block_size] for i in range(0, len(ciphertext), AES.block_size)]

    for c in range(1, len(ciphertext_blocks)):
        plaintext_block = b''   # This is the part of plaintext corresponding to each ciphertext block

        # Take each character of the ciphertext block (starting from the last one)
        # and decrypt it by forcing the previous block as IV.
        for i in range(AES.block_size - 1, -1, -1):

            # The padding len for the current character will depend on how many characters of this
            # block (starting from the right), we have already decrypted.
            padding_len = len(plaintext_block) + 1

            # Find each possible character which gives us a correct padding
            possible_last_bytes = []
            for j in range(256):

                # Create a IV with the guessed character j
                forced_iv = create_forced_previous_block(ciphertext_blocks[c - 1], j, padding_len, plaintext_block)

                # If the guessed character j gave us a working padding, save it as one of the candidates
                if oracle.decrypt_and_check_padding(ciphertext_blocks[c], forced_iv) is True:
                    print("foudn something")
                    possible_last_bytes += bytes([j])

            # In case of ambiguity, if we found more than one candidate, we can choose the best by trying
            # to force the next character too.
            #
            # This is useful because, for example, if we were trying to find the last character
            # of this plaintext (which was already padded):
            #
            #     123456789012/x04/x04/x04/x04
            #
            # There would be two possible last characters that form a valid padding (/x01 and /x04).
            # However if we try the next character too, we can easily choose the correct one.
            if len(possible_last_bytes) != 1:
                for byte in possible_last_bytes:
                    for j in range(256):
                        forced_iv = create_forced_previous_block(ciphertext_blocks[c - 1], j, padding_len + 1,
                                                                 bytes([byte]) + plaintext_block)

                        # If we manage to get a valid padding, then it's very likely that this
                        # candidate is the one that we want. So exclude the others and exit the loop.
                        if oracle.decrypt_and_check_padding(ciphertext_blocks[c], forced_iv) is True:
                            possible_last_bytes = [byte]
                            break
            if(len(possible_last_bytes)==0):
                print("foudn nothing")
            # Got the new byte of the plaintext corresponding to the block we are decrypting,
            # add it on top of the decrypted text.
            plaintext_block = bytes([possible_last_bytes[0]]) + plaintext_block

        # Add the block we have decrypted to the final plaintext
        plaintext += plaintext_block

    # Return the unpadded plaintext bytes (in base 64)
    return padding_validation.pkcs7_unpad(plaintext)


def main():
    oracle = Oracle(texts)
    result = attack_padding_oracle(oracle.get_encryption_message(), oracle)

    # Print the decryption of the message that was chosen. If it's human readable then the attack worked.
    # The numbers at the beginning are normal and they are present in every ciphertext of the input file
    print(base64.b64decode(result.decode()))

if(__name__ == '__main__'):
    main()
