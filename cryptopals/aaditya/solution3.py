import frequency
import sys

# string xor equal length
def sxor(s1, s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

# xor with char
def xor_char(char, string):
	decrypt = ''
	for x in string.lower():
		decrypt += sxor(char, x)
	return decrypt

hex_inp = sys.argv[1]
byte_inp = hex_inp.decode('hex')

scores = {}
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .\'",?!'
for chars in characters:
        decrypt = xor_char(chars, byte_inp)
        scores[chars] = frequency.score(repr(decrypt))

scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

for x in scores[:5]:
	print "This key %s generates %s plaintext with %s confidence" %(x[0], repr(xor_char(x[0],byte_inp)), x[1])
