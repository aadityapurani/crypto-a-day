#!/usr/bin/python
# YunnyIT Task

from base64 import *
from Crypto import Random
from Crypto.Cipher import AES
from secret import FLAG, key
from hashlib import *
import hmac
import sys, os, signal, string
import random
import inspect

def genrandstr(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))

def isprintable(mystr):
    return all(c in string.printable for c in mystr)

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

class AESCipher:
    
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        iv = Random.new().read(AES.block_size)
        digest = hmac.new(self.key, iv + raw, sha1).digest()
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(pad(raw + digest)))

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain = unpad(cipher.decrypt(enc[BLOCK_SIZE:]))
        raw, digest = plain[:-20], plain[-20:]
        if hmac.new(self.key, iv + raw, sha1).digest() == digest:
            return raw
        else:
            raise Exception

    def EFoF(self, suffix, prefix):
        assert len(FLAG) == 32
        assert len(self.key) == 16
        return AESCipher(self.key).encrypt(suffix + FLAG + prefix)

def main():
    pr("|-------------------------------------|")
    pr("| Welcome to the Yunnyit crypto task! |")
    pr("|-------------------------------------|")
    pr("| Options: 			      |\n| [M]ixed encryption function of FLAG |\n| [D]ecrypting cipher        	      |\n| [E]ncryption & decryption function  |\n| [F]LAG encrypting...                |\n| [Q]uit		  	      |")
    pr("|-------------------------------------|")
    while True:
        pr("Send your Options:")
        ans = raw_input().strip().lower()
        if ans == 'm':
            pr(inspect.getsource(AESCipher.EFoF))
        elif ans == 'f':
            pr('Send the prefix:')
            prefix = raw_input().strip()
            pr('Send the suffix:')
            suffix = raw_input().strip()
            if suffix != '' and prefix != '':
                enc = AESCipher(key).encrypt(suffix + FLAG + prefix)
                pr('Mixed encrypted FLAG =', enc)
            else:
                pr('You must send non-empty suffix and prefix, Bye!!')
        elif ans == 'd':
            pr('Send the cipher please:')
            enc = raw_input().strip()
            try:
                enc = b64decode(enc)
                iv = enc[:BLOCK_SIZE]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                raw = cipher.decrypt(enc)
                if FLAG in raw:
                    pr('Great job :D')
                else:
                    pr('Catch FLAG if you can :P')
            except:
                pr('What?????')
        elif ans == 'e':
            pr(inspect.getsource(AESCipher.encrypt), '\n', inspect.getsource(AESCipher.decrypt)) 
        elif ans == 'q':
            die("Quiting ...")
        else:
            die('You should have valid choise, Bye!')

def die(*args):
    pr(*args)
    quit()

def pr(*args):
    s = " ".join(map(str, args))
    sys.stdout.write(s + "\n")
    sys.stdout.flush()

def sc():
    return sys.stdin.readline().strip()

if __name__ == '__main__':
    main()
