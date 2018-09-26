# Aaditya's Solution


##### Challenge 1

We decode hexadecimal and then we encode it to base64

```
import base64
a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
a_dec = a.decode('hex')
print base64.b64encode(a_dec)
```

##### Challenge 2

This is a fixed length xor, so without cheating (aka using pwntools xor, crypto) I implemented by owon xor function

```
def xor_fixed(a, b):
	if len(a) == len(b):
		a_dec = a.decode('hex')
		b_dec = b.decode('hex')
		final_string = ""
		for i in xrange(0, len(a_dec)):
			final_string += chr(ord(a_dec[i])^ord(b_dec[i]))
		final_string_encode = final_string.encode('hex')
		return final_string_encode

xor_fixed("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")
```
