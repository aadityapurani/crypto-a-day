def add_to_buffer(s,buffer_size,buffer_char = None):
	dif = (buffer_size-len(s))%buffer_size
	if(buffer_char == None):
		buffer_char = hex(dif)
	return s + buffer_char * (dif)

def main():
	s = 'YELLOW SUBMARINE'
	buffer_size = 20
	return add_to_buffer(s,buffer_size)