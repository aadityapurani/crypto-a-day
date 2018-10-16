import hashpumpy
import re
from pwn import *

'''
hashpump(hexdigest, original_data, data_to_add, key_length) -> (digest, message)
'''

context.log_level='DEBUG'

r = remote('127.0.0.1', 8000)
r.recvuntil('xit\n')
r.sendline('2')
r.recvuntil('ID: ')
r.sendline('5')
r.recvline()
order = r.recvline().decode().strip()
(order_orig, signature) = re.match(r"(.*)&sign=([a-f0-9]+)", order).groups()

# As the signkey will be always between 8 to 32 rand
for i in range(8, 32):
        (new_hash, new_message) = hashpumpy.hashpump(signature, order_orig, "&price=0", i)
        r.recvuntil('xit\n')
        r.sendline('3')
        r.recvline()
        r.sendline(new_message+"&sign="+new_hash.encode())
        r.recvline()
        msg = r.recvline().decode().strip()
        print msg
        if 'Invalid' not in msg:
        	r.recvall()
