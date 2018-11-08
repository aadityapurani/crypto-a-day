from pwn import process, remote
from base64 import b64encode
from hashlib import sha256
from string import printable
from functools import partial
from itertools import count, islice, izip, tee, takewhile, imap

def get_digest_from_tube(io, x):
  io.recvuntil('Quit\n')
  io.sendline('1')
  io.recvline()
  io.sendline(b64encode(x))
  return int(io.recvline())

def matches(get_digest): 
  # get the sha256 of the flag by digesting 0
  key_hash = get_digest('\x00')

  key = 0
  for i in count():
    # get sha256((flag ^ 2**i) + 2^i) from the server 
    digest = get_digest(from_int(2**i))
    # test if the ith bit is set in the flag and it to the key if it is
    if digest == key_hash:
      key = key ^ 2**i 
    print(i)
    # if we have tested a multiple of 8 bits, yield the answer so far
    if i % 8 == 0:
      yield from_int(key)

def main(): 
  print('Starting to pwn')
  io = remote('localhost', 8000)
  # io = process(['python',  'server.py'])
  get_digest = partial(get_digest_from_tube, io)
  curr, prev = tee(matches(get_digest))
  print(curr,prev)
  prev       = islice(prev, 1, None)
  not_equal  = lambda (x, y): x != y
  second     = lambda (x, y): y

  # keep printing the partial flag until we have found the entire flag
  for x in imap(second, takewhile(not_equal, izip(curr, prev))):
    print(x)

def from_int(i):
    ''' inverse of the to_int function on the server '''
    h = hex(i)[2:]
    h = h if len(h) % 2 == 0 else '0' + h
    return h.decode('hex')

if __name__ == "__main__":
  main()