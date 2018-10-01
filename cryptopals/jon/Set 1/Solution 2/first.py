import base64
def solution():
	#get data
	a = "1c0111001f010100061a024b53535009181c"
	b = "686974207468652062756c6c277320657965"
	
	#decode each
	a_dec = a.decode('hex')
	b_dec = b.decode('hex')

	#xor each and insert into array
	result_array=[char(ord(ai)^ord(bi)) for ai,bi in zip(a_dec,b_dec)]
	result_dec = "".join(result_array)
	#encode back to b16
	result = base64.b16encode(result_dec)

