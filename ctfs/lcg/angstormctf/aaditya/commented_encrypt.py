import struct

# m, x known
def lcg(m, a, c, x):
	return (a*x + c) % m

m = pow(2, 32)	# m is known

with open('lcg') as f:
	a = int(f.readline())
	c = int(f.readline())
	x = int(f.readline())

d = open('flag.png').read() # Opens file for reading
d += '\x00' * (-len(d) % 4)	# Appends null byte if totalsize is not multiple of 4
d = [d[i:i+4] for i in range(0, len(d), 4)]	# Group 4 bytes and append to a list

e = ''
for i in range(len(d)):
	e += struct.pack('>I', x ^ struct.unpack('>I', d[i])[0])
	x = lcg(m, a, c, x)			# x changes everytime, but for first encrypt it will be the one from file

with open('flag.png.enc', 'w') as f:
	f.write(e)
	f.close()
