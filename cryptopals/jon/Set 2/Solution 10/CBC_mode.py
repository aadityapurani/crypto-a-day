import sys
import os
sys.path.insert(0,os.getcwd()+'\\src')
import add_to_buffer
def main():
	block_size = 32
	
	IV = 'fake 0th ciphertext block' #initialization_vector
	string = "Hello world"
	# split the string