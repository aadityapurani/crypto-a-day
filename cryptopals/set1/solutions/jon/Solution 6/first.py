from collections import Counter
import base64

def solution():
	f=open("code.txt",'r')
	str = "".join(f.read().split('\n'))
	f.close()
	keySize = findKeySize(str)
def findKeySize(str):
	bestKeySize = 2
	#first,second = str[0:2],str[3:5],str[6-8] str[9-11]
	#print levenshteinDistance(first,second)/float(2)
	MAX_KEYSIZE = 40
	arr = [0 for x in range(len(str))]
	for i in range(0,len(str),2*2+2):
		#print('hi')
		#print(str[i,i+2])
		arr[i] = levenshteinDistance(str[i:i+2],str[i+3:i+5])
	print(arr)
	#for test_KS in range(2,MAX_KEYSIZE):
		
def convertToBinaryString(string1):
	str = ""
	for l in string1:
		bi = bin(ord(l))[2:]
		str += "0"*(8-len(bi))+bi
	return str

def hammingDistance(string1,string2):
	if(len(string1)!=len(string2)):
		raise ValueError("Undefined for sequences of unequal length")
	distance = 0
	
	distance = sum(b1!=b2 for b1,b2 in zip(string1,string2))
	return distance

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
	
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # isnert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 

def x():
	return 2