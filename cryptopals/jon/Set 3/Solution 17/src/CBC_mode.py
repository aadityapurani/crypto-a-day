import os
import sys
sys.path.insert(0,os.getcwd()+'/src')
import useful_functions
from Crypto.Cipher import AES

def aes_128_ecb_enc(buffer,key):
	obj = AES.new(str(key), AES.MODE_ECB)
	return bytearray(obj.encrypt(bytes(buffer)))

def aes_128_ecb_dec(buffer,key):
	obj = AES.new(str(key), AES.MODE_ECB)
	return bytearray(obj.decrypt(bytes(buffer)))

def aes_128_cbc_enc(buffer,key,iv):
	plain_text = useful_functions.pad_pkcs7(buffer,AES.block_size)
	cipher_text = bytearray(len(plain_text))
	prev_one = iv
	#print('plaintext',type(plain_text))
	#print('buffer',type(buffer))
	#print('iv',type(iv))
	#print('key',type(key))
	for i in range(0,len(plain_text),AES.block_size):
		#print(i)
		cur_sec = plain_text[i:i+AES.block_size]
		xor_sec = useful_functions.xor(cur_sec,prev_one)
		#print('about to encrypt')
		enc_sec = aes_128_ecb_enc(xor_sec,key)
		cipher_text[i:i+AES.block_size] = enc_sec
		prev_one = cipher_text[i:i+AES.block_size]
	#print("finished")
	return cipher_text

def aes_128_cbc_dec(cipher_text,key,iv):
	plain_text = bytearray(len(cipher_text))
	prev_one = iv
	for i in range(0,len(plain_text),AES.block_size):
		#print('hi')
		cur_sec = cipher_text[i:i+AES.block_size]
		dec_sec = aes_128_ecb_dec(bytes(cur_sec),key)
		xor_sec = useful_functions.xor(dec_sec,prev_one)
		plain_text[i:i+AES.block_size] = xor_sec
		prev_one = cipher_text[i:i+AES.block_size]
	return useful_functions.unpad_pkcs7(plain_text)

if(__name__ == '__main__'):
	iv = bytearray("fake 0th ciphertext block")
	key = "YELLOW SUBMARINE"
	#print('hi')
	cipher_text = bytearray("".join(list(open("10.txt"))).decode("base64"))
	print(aes_128_cbc_dec(cipher_text,key,iv))
