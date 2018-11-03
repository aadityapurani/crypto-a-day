import gmpy2
import gmpy
import codecs
from Crypto.PublicKey import RSA
import base64
from itertools import cycle, izip


target_file = "kStoynmN5LSniue0nDxli9csSrBgexZ/YOo5e+MUkfJKwvht8hHsYyMGVYzMlOp9sAFBrPCbm4UA4n7oMr2zlg=="
target_dec = base64.b64decode(target_file)

enc_key = 219135993109607778001201845084150602227376141082195657844762662508084481089986056048532133767792600470123444605795683268047281347474499409679660783370627652563144258284648474807381611694138314352087429271128942786445607462311052442015618558352506502586843660097471748372196048269942588597722623967402749279662913442303983480435926749879440167236197705613657631022920490906911790425443191781646744542562221829319509319404420795146532861393334310385517838840775182

with codecs.open('pubkey.pem') as fr:
	pub = fr.read()
	pub = RSA.importKey(pub)

print "[+] n = "+str(pub.n)
print "[+] e = "+str(pub.e)

gs = gmpy.mpz(enc_key)
gm = gmpy.mpz(pub.n)
g3 = gmpy.mpz(pub.e)
meh = gs+gm

# we go on like c+n , c+2*n etc until we hit _ = True
 
root, _ = meh.root(g3)
#print _
kek = hex(int(root))[2:-1].decode('hex')

print len(hex(int(root))[2:-1].decode('hex'))

assert len(target_dec) == len(hex(int(root))[2:-1].decode('hex'))
flaglol= ''.join(chr(ord(c)^ord(k)) for c,k in izip(target_dec, cycle(kek)))
print flaglol
