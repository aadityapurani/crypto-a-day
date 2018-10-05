from pwn import *
from crypto_commons.symmetrical.symmetrical import oracle_padding_recovery
# https://github.com/p4-team/crypto-commons/

def oracle(ct):
    r = remote('2018shell3.picoctf.com', 45008)
    r.recvuntil('cookie?')
    r.sendline(ct)
    r.recvline()
    d = r.recvline()
    print d
    r.close()
    if 'invalid padding' in d:
    	return False
    elif 'Traceback' in d:
	return True
    else:
    	return True


def main():
    ct = '5468697320697320616e20495634353642fef6c675ee50fca505d4023e8c21bd0b409a1f864eec9dad32e86199b518330ab686ba7afaf345e4b2bdca541146511d82c37e7f991be60eda932d1fd407c65ab1726c337c128163c4c3449ce2398d'
    oracle_padding_recovery(ct, oracle)


main()
