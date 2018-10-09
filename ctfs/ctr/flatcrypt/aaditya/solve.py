from pwn import *
import string

#context.log_level='DEBUG'

charset_flag = string.ascii_lowercase + '_'
padding = 'ABCDEFGHIJKLMNOPQRST'

r = remote('127.0.0.1', 8040)
known_flag = ''

while True:
    bestchar = None
    lowestlen = 9999
    worstlen = -1

    for c in charset_flag:
        send_this =  padding + c + known_flag + padding
        r.recvuntil('ervice')
        r.sendline(send_this)
        r.recvline().strip()
        x = r.readline().strip()
        reslen = ord(x[-1])
        if reslen < lowestlen:
            lowestlen = reslen
            bestchar = c
        worstlen = max(reslen, worstlen)

    if worstlen == lowestlen:
        break

    known_flag = bestchar + known_flag
    print known_flag
