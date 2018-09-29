import string
from pwn import *

#context.log_level='DEBUG'
# I tested on my own VPS, I have took the server down.
# You can buy a digital ocean VPS and run that python source code using 
# socat -T60 TCP-LISTEN:8000,reuseaddr,fork EXEC:"python -u ./baby_crypt.py"

r = remote('mydomain.com', 8000)

final_flag = ""

for k in range(0,3):
	current_prog= ""
	for i in xrange(0,16):
		nice_payload = 'a'*(15-i)
		r.recvuntil("space):")
		r.sendline(nice_payload)
		guess_char =  r.recvline()[17:]
		guess_char = guess_char[:32+32*k]

		print "Bruting the "+str(i+1)+" character"
		for x in string.printable:
			first_payload='a'*(15-i)
			r.recvuntil("space):")
			r.sendline(first_payload+final_flag+current_prog+x)
			newly_char = r.recvline()[17:]
			newly_char = newly_char[:32+32*k]
			if newly_char == guess_char:
				current_prog +=x
				print current_prog
				break
	final_flag += current_prog
	print final_flag
