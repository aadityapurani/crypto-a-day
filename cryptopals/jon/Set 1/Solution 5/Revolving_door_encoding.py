import base64
def xor_revolving_door(input1,xor_string):
	decoded_input = input1
	xrd= [ord(x) for x in xor_string]
	result = ""
	for i in range(len(decoded_input)):
		x = decoded_input[i]
		char = chr(ord(x)^xrd[i%len(xrd)])
		i+=1
		result+=char
	return result
def solution():
	input1 = "Hi my name is jon! I'm the coolest guy in the street"
	xor_string = "Ice ice baby"
	result = xor_revolving_door(input1,xor_string)
	return result