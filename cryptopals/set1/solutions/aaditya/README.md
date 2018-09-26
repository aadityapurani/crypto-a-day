# Aaditya's Solution


##### Challenge 1

We decode hexadecimal and then we encode it to base64

```
import base64
a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
a_dec = a.decode('hex')
print base64.b64encode(a_dec)
```
