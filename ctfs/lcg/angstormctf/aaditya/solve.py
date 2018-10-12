import struct
import gmpy

# 89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52
# other params to lcg are known

def lcg(m, a, c, x):
	return (a*x + c) % m

m = pow(2,32)

png_chunk1 = 0x89504e47
png_chunk2 = 0x0d0a1a0a
png_chunk3 = 0x0000000d
png_chunk4 = 0x49484452

d = open('flag.png.enc').read()
d = [d[i:i+4] for i in range(0, len(d), 4)]	

x0 = png_chunk1 ^ struct.unpack('>I', d[0])[0]
x1 = png_chunk2 ^ struct.unpack('>I', d[1])[0]
x2 = png_chunk3 ^ struct.unpack('>I', d[2])[0]
x3 = png_chunk4 ^ struct.unpack('>I', d[3])[0]

a =  (x2 - x1)*gmpy.invert(x1 - x0, m)%m
c = (x1 - a*x0)%m

x = x0

known = ''
for i in xrange(len(d)):
	known += struct.pack('>I', x ^ struct.unpack('>I', d[i])[0])
	x = lcg(m, a, c, x)

with open('flag.png', 'w') as f:
	f.write(known)
	f.close()
