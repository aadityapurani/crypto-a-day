def solution():
	f=open("code.txt")
	code = f.read()
	f.close()
	return len(code.split('\n'))

def splitString(str1,split_by= 2):
	#str1 = strl[j:j+i]
	#str2 = strl[j+i+1:j+i*2+1]
	return [str1[i:i+split_by] for i in range(0,len(str1),split_by)]
	
	