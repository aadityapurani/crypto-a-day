from collections import Counter
import base64

def solution():
	string1 = "this is a test"
	string2 = "wokka wokka!!!"
	bin_string1,bin_string2=convertToEvenBinaryString(string1,string2)
	#bin_string1 = convertToBinaryString(string1)
	#bin_string2 = convertToBinaryString(string2)
	#return editDistDP(bin_string1,bin_string2,len(bin_string1),len(bin_string2))
	return hammingDistance(bin_string1,bin_string2)
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
