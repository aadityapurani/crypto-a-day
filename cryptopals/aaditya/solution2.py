#!/usr/bin/python
def xor_fixed(a, b):
	if len(a) == len(b):
		a_dec = a.decode('hex')
		b_dec = b.decode('hex')
		final_string = ""
		for i in xrange(0, len(a_dec)):
			final_string += chr(ord(a_dec[i])^ord(b_dec[i]))
		final_string_encode = final_string.encode('hex')
		return final_string_encode

xor_fixed("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")
