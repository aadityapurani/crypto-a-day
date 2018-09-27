#How to devise scoring?
#if it has number followed by anything but a puntuation, number or space it's wrong.
#first divide up the words
import base64
import string


#A Greedy solution
def solution():
	#get data
	f = open("code.txt",'r')
	arr = f.read();
	f.close();
	arr=arr.split("\n");
	#print(len(arr[0]))
	printable = [x for x in string.printable]
	usable_chars_in_words = string.uppercase+string.lowercase+'\n'+' '
	vowels = "AEIOUYaeiouy"
	vowels_arr = [x for x in vowels]
	
	#decode a
	arr_dec = [a.decode('hex') for a in arr]
	#print([len(x) for x in arr_dec])
	accepted = 0
	accepted_now = []
	for key in range(256):
		#xor each and insert into array
		test_array=["".join([chr(ord(ai)^key) for ai in a_dec]) for a_dec in arr_dec]
		rejected = []
		#print([len(x) for x in test_array])
		#check if the string is printable
		cur_avg = 0
		for test_dec in test_array:
			flag =  False
			#sum = 0
			if(not all(letter in printable for letter in test_dec)):
				continue
			#for letter in test_dec:
			#	if(letter not in printable):
			#		flag = True
			#		#sum+=1
			#if(flag):
				#cur_avg += sum
				#rejected.append(True)
			#	continue
			#the longest word in english is 45 letters
			#check if there is a reasonable number of spaces
			if(len(test_dec)/45.0>=test_dec.count(" ")):
			#	rejected.append(True)
				continue
			
			#check if each spaced word has atleast one vowel
			#split the words by space
			set_of_words= test_dec.split(" ")
			for word in set_of_words:
				if(all(char in usable_chars_in_words for char in word)):
					continue
				flag = True
			if(flag):
				continue
			accepted_now.append(test_dec)
		#print(cur_avg,key)
		#if(len(rejected)<10):
		#	accepted+=1
		#else:
		#	print(len(rejected))
		#if(key==127):
		#	print(test_array)
	return accepted_now

