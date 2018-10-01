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
##### Challenge 3
Single byte xor against cipher-text and identifying using frequency analysis what string has maximum points

```
python solution3.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
This key X generates "Cooking MC's like a pound of bacon" plaintext with 2.2641049 confidence
This key r generates 'iEEACDM\ngi\rY\nFCAO\nK\nZE_DN\nEL\nHKIED' plaintext with 1.6352478 confidence
This key v generates 'mAAEG@I\x0ecm\t]\x0eBGEK\x0eO\x0e^A[@J\x0eAH\x0eLOMA@' plaintext with 1.6301552 confidence
This key R generates 'Ieeacdm*GI-y*fcao*k*ze\x7fdn*el*hkied' plaintext with 1.267941 confidence
This key 9 generates '"\x0e\x0e\n\x08\x0f\x06A,"F\x12A\r\x08\n\x04A\x00A\x11\x0e\x14\x0f\x05A\x0e\x07A\x03\x00\x02\x0e\x0f' plaintext with 1.1823283 confidence
```

##### Challenge 5
`izip` and `cycle` does the trick for us
```
python solution5.py "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" "ICE"
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20152d0c69242a69203728393c69342d2c2d6500632d2c22376922652a3a282b2229
```
