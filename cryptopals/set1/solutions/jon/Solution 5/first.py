import base64

def solution(input1 = "Hi my name is jon! I'm the coolest guy in the street",xor_string = "Ice ice baby"):
	#input1 = "Hi my name is jon! I'm the coolest guy in the street"
	#decoded_input = base64.b16decode(input)
	decoded_input = input1
	#xor_string = "Ice ice baby"
	xor_revolving_door = [ord(x) for x in xor_string]
	i = 0
	result = ""
	for i in range(len(decoded_input)):
		x = decoded_input[i]
		char = chr(ord(x)^xor_revolving_door[i%len(xor_revolving_door)])
		i+=1
		result+=char
	return result