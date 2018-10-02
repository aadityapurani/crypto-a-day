import string
from pwn import *

'''
48 bytes = 16 * 3 = 3 blocks
Blocks indpendent in ECB
'''

charset = '{_}' + string.ascii_lowercase + string.digits

#context.log_level='DEBUG'

r = remote('chal1.swampctf.com', 1450)

flag =''


# Cuz it's custom RTL Padding and it's pain
for k in range(2):
	blk = ['A']*16
	for i in range(16):
		for c in charset:
			blk[i] = c
			flag_blk = 'A'*(15-i)
			m =  flag_blk + ''.join(blk)
			m += 'A' * (47-len(m) - i -16*k)
			r.sendline(m)
			n = r.recvline().strip().decode('hex')
			if n[0+16*k:16+16*k] == n[16+16*k:32+16*k]:
				flag += c
				print flag
				break

blk = ['A']*16
for i in range(16):
	flag_blk = 'A'*(15-i)
	r.sendline(flag_blk)
	n = r.recvline().strip().decode('hex')
	lol = n[32:48]
	for c in charset:
		blk[i] = c
		r.sendline(''.join(blk))
		n = r.recvline().strip().decode('hex')
		if n[32:48] == lol:
			flag +=c
			print flag
			break
