def solution():
	f=open("code.txt")
	code = f.read()
	f.close()
	return len(code.split('\n'));