from Crypto.Cipher import AES

def add_to_buffer(s,buffer_size,buffer_char = None):
	dif = (buffer_size-len(s))%buffer_size
	if(buffer_char == None):
		buffer_char = hex(dif)
	return s + buffer_char * (dif)

def split_string(s,split_size):
	size = len(s)/split_size+1
	result = [s[split_size*i:split_size*(i+1)] for i in range(0,size)]
	if(len(result[-1])==0):
		result.pop()
	return result

#converts a string to binary
def convert_to_binary(s):
	result = ""
	for let in s:
		cur = bin(ord(let))[2:]
		cur = '0'*(8-len(cur)) + cur
		result += cur
	return result

def xor(b1, b2):
    b = bytearray(len(b1))
    #print(b1,b2)
    for i in range(len(b1)):
        #print(b1[i],b2[i])
        b[i] = b1[i] ^ b2[i]
    return b

def xor_strings(s1,s2):
	if(len(s1)!=len(s2)):
		raise ValueError("s1 and s2 have unequal lengths")
	result = ""
	for i1,i2 in zip(s1,s2):
		result += chr(ord(i1)^ord(i2))
	return result

def pad_pkcs7(buffer, block_size):
    if len(buffer) % block_size:
        padding = (len(buffer) / block_size + 1) * block_size - len(buffer)
    else:
        padding = 0
    # Padding size must be less than a byte
    assert 0 <= padding <= 255
    new_buffer = bytearray()
    new_buffer[:] = buffer
    new_buffer += bytearray([chr(padding)] * padding)
    return new_buffer

def unpad_pkcs7(buffer):
    padding = buffer[-1]
    for i in range(len(buffer) - 1, len(buffer) - padding - 1, -1):
        if buffer[i] != buffer[-1]:
            return buffer
    new_buffer = bytearray()
    new_buffer[:] = buffer[:-padding]
    return new_buffer

def unpad_valid_pkcs7(buffer):
    padding = buffer[-1]
    if padding >= AES.block_size:                  
        return buffer  
    for i in range(len(buffer)-1, len(buffer)-padding, -1):
        if buffer[i] != buffer[-1]:
            raise Exception("Bad PKCS#7 padding.")
    new_buffer = bytearray()
    new_buffer[:] = buffer[:-padding]
    return new_buffer

def is_pkcs7_padded(binary_data):
    """Returns whether the data is PKCS 7 padded."""

    # Take what we expect to be the padding
    padding = binary_data[-binary_data[-1]:]

    # Check that all the bytes in the range indicated by the padding are equal to the padding value itself
    return all(padding[b] == len(padding) for b in range(0, len(padding)))
