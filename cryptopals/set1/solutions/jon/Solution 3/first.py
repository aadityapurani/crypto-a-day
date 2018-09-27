#How to devise scoring?
#if it has number followed by anything but a puntuation, number or space it's wrong.
#first divide up the words
import base64
import string


#A Greedy solution
def solution():
	#get data
	a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	printable = [x for x in string.printable]
	#decode a
	a_dec = a.decode('hex')
	accepted = []
	for key in range(256):
		#xor each and insert into array
		test_array=[chr(ord(ai)^key) for ai in a_dec]
		test_dec = "".join(test_array)
		
		#check if the string is printable
		flag=  False
		for let in test_dec:
			if(let not in printable):
				flag = True
				break
		if(flag):
			continue
		
		#the longest word in english is 45 letters
		#check if there is a reasonable number of spaces
		if(len(a)/45.0>test_dec.count(" ")):
			continue
		accepted.append(test_dec)
		
	return accepted

