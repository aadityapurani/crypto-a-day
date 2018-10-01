import sys
from itertools import izip, cycle

message = sys.argv[1]
key = sys.argv[2]

def rep_xor(s1, s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in izip(message,cycle(key)))

final = rep_xor(message, key)
print final.encode('hex')
