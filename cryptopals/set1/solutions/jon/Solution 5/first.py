import base64

def solution():
	input1 = _______
	decoded_input = base64.b16decode(input)
	xor_string = "Ice"
	xor_revolving_door = [ord(x) for x in xor_string]
	i = 0
	result = ""
	for i in range(len(decoded_input)):
		x = decoded_input[i]
		char = chr(ord(x)^xor_revolving_door[i++%len(xor_revolving_door)])
		result+=char
	return result