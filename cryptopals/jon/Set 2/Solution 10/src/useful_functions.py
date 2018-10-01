def add_to_buffer(s,buffer_size,buffer_char = None):
	dif = (buffer_size-len(s))%buffer_size
	if(buffer_char == None):
		buffer_char = hex(dif)
	return s + buffer_char * (dif)
def split_string(s,split_size):
	size = len(s)/split_size+1
	result = [s[split_size*i:split_size*(i+1)] for i in range(0,size)]
	if(len(result[-1])==0):
		result.pop()
	return result