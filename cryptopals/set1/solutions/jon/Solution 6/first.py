from collections import Counter
import base64

def solution():
	string1 = "this is a test"
	string2 = "wokka wokka!!!"
	bin_string1,bin_string2=convertToEvenBinaryString(string1,string2)
	#bin_string1 = convertToBinaryString(string1)
	#bin_string2 = convertToBinaryString(string2)
	return edit_distance(bin_string1,bin_string2)

#calculates the hamming distance

def convertToBinaryString(string1):
	str = ""
	for l in string1:
		str += bin(ord(l))[2:]
	return str
def convertToEvenBinaryString(string1,string2):
	str1,str2 = "",""
	for l1,l2 in zip(string1,string2):
		b_l1,b_l2 = bin(ord(l1))[2:],bin(ord(l2))[2:]
		l_b1,l_b2 = len(b_l1),len(b_l2)
		dl = l_b1-l_b2
		if(dl>0):
			b_l2 = "0"*dl+b_l2
		elif(dl<0):
			b_l1 = "0"*(-dl)+b_l1
		str1+=b_l1
		str2+=b_l2
	return str1,str2

def hammingDistance(string1,string2):
	if(len(string1)!=len(string2)):
		raise ValueError("Undefined for sequences of unequal length")
	distance = 0
	
	distance = sum(b1!=b2 for b1,b2 in zip(string1,string2))
	return distance
#Very bad
#def LD(s, t):
#    if s == "":
#        return len(t)
#    if t == "":
#        return len(s)
#    if s[-1] == t[-1]:
#        cost = 0
#    else:
#        cost = 1
#       
#    res = min([LD(s[:-1], t)+1,
#               LD(s, t[:-1])+1, 
#               LD(s[:-1], t[:-1]) + cost])
#    return res
	
#doesn't work

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
	
def edit_distance(s1,s2):
	l1,l2 = len(s1),len(s2)
	arr = [[0 for i in range(l1+1)] for j in range(l2+1)]
	for i in range(l2+1):
		arr[i][0] = i
	for j in range(l1+1):
		arr[0][j] = j
	
	return arr