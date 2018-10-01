from collections import Counter
import base64
import frequency

def solution(x=None):
	f=open("code.txt",'r')
	str = "".join(f.read().split('\n'))
	#return str
	f.close()
	div_cypher = x
	if(x==None):
		keySizeArray = findKeySize(str)
		div_cypher = divideCypher(str,keySizeArray)
	tran_text = transpose(div_cypher)
	min = 10000
	lowest_key = -1
	#need to add min array
	#need to add lowest_key_array
	#need to add lowest key array for each set
	for i in range(len(tran_text)):
		cur_key_size = tran_text[i]
		for key in range(256):
			for str in cur_key_size:
				sol = "".join([chr(ord(char)^key) for char in str])
				sco = frequency.score(sol)
				if(sco<min):
					min = sco
					lowest_key = key
	print(min,lowest_key)
	sol = "".join([chr(ord(char)^key) for char in str])
	return sol
				#test_array=[chr(ord(ai)^key) for ai in a_dec]
def transpose(L):
	transposed_array = [["" for _ in range(len(L[i][0]))] for i in range(len(L))]
	for i in range(len(L)):
		item = L[i]
		for j in range(len(item)):
			str = item[j]
			#print(i,j,len(str))
			for k in range(0,len(str)):
				char = str[k]
				transposed_array[i][k]+=char
	return transposed_array
#returns a list of respective blocks
def divideCypher(str,E):
	L = [[] for _ in range(len(E))]
	for i in range(len(E)):
		stuff = E[i]
		print(stuff)
		size = stuff[1]
		for j in range(0,len(str),size+1):
			L[i].append(str[j:j+size])
	return L

def findKeySize(strl):
	MAX_NUM = 10000
	bestKeySize = 2
	MAX_KEYSIZE = 40
	arr = [0 for x in range(len(strl))]
	
	L = [[MAX_NUM,-1] for _ in range(4)]
	for i in range(2,40):
		count = 0.0
		sum = 0.0
		for j in range(0,len(strl),i*2+2):
			count+=1.0
			str1 = strl[j:j+i]
			str2 = strl[j+i+1:j+i*2+1]
			bt1 = convertToBinaryString(str1)
			bt2 = convertToBinaryString(str2)
			sum+= levenshteinDistance(bt1,bt2)/i
		print(i, sum/count)
		minList(L,sum/count,i)
	return L

def minList(L,test,index):
	min = -1
	#find it
	for i in range(len(L)):
		if(L[i][0]>test):
			min = i
			break
	if(min==-1):
		return
	#make stuff tickle down
	for i in range(len(L)-2,min-1,-1):
		L[i+1] = L[i]
	L[min] = [test,index]

def maxList(L,test,index):
	max = -1
	#find it
	print("List: {}".format(L))
	for i in range(len(L)-1,0,-1):
		print("Testing {} > {}".format(L[i][0],test))
		if(L[i][0]>test):
			max = i
			break
	#print("found max ",max)
	if(max==-1):
		return
	print(max)
	#make stuff tickle down
	for i in range(len(L)-1,max,-1):
		print("switching: ",L[i-1],L[i])
		L[i] = L[i-1]
	L[max+1] = [test,index]
	
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