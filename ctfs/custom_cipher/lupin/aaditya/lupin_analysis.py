#!/usr/bin/env python2
import json
import numpy as np
import os
import reedsolo
import struct

flag = 'flag{To get the real flag, solve the problem against the live server.}'

randprob = lambda: float(struct.unpack('<Q', os.urandom(8))[0])/2**64
product = lambda xs: reduce(lambda a, b: a*b, xs, 1)
randprobmat = lambda shape: np.array([randprob() for _ in range(product(shape))]).reshape(shape)
randbitmat = lambda shape: (randprobmat(shape)<0.5)&1
ber = lambda k, t: (randprobmat(k)<t)&1

# Most reverse functions are provided
unpack = lambda s: list(__import__('itertools').chain(*[[1&(ord(c)>>i) for i in range(8)] for c in s]))
pack = lambda x: (lambda t: ''.join(chr(sum(t[8*i:8*i+8])) for i in range(len(t)/8)))([(b<<(i%8)) for i,b in enumerate(x)])
serialize_mat = lambda X: '%s;%s' % (','.join(str(i) for i in X.shape), pack(X.reshape((product(X.shape),))).encode('base64'))
deserialize_mat = lambda s: (lambda (dims,data): np.array(unpack(data.decode('base64'))).reshape(map(int,dims.split(','))))(s.split(';'))

def MultiBitKeyGen(n):
    t = 1.0/n                                   # Very low probability 0.00125
    S = randbitmat((n, n))                      # Create random matrix of 800x800
    A = randbitmat((2*n, n))                    # Create random matrix of 1600x800
    E = ber((2*n, n), t)                        # Most likely 1600x800 0 matrice eh?
    B = (A.dot(S) + E) % 2                      # Dot product B = A.S
    return {'pk': (A, B, t), 'sk': S}           # Public Key -- A,B,t ; Secret key -- S

def MultiBitEnc((A, B, t), s):                  # Secret key s is passed, which has bit error proof
    n = A.shape[1]                              # Number of columns           
    v = unpack(s)                               # Converts to binary 8 bit representation of each ASCII (i.e flag)
    f = ber((2*n,), t)                          #       
    u = f.T.dot(A) % 2                          # Transpose of f and then taking dot with A. So size will be like f
    c = (f.T.dot(B) + np.array(v+[0]*(n-len(v))).T) % 2 # c = f.T.dot(B) + v
    return (u, c)

def MultiBitDec(S, (u,c)):
    d = (c + S.T.dot(u)).T % 2
    return pack(d)

def serialize_key(key):
    (A,B,t) = key['pk']
    S = key['sk']
    ser = {'pk': (serialize_mat(A), serialize_mat(B), t), 'sk': serialize_mat(S)}
    return json.dumps(ser)          # Serialized solution

def get_values(m):
    rs_bytes = 20
    codec = reedsolo.RSCodec(rs_bytes)
    try:
        with open("lpn.key", "r") as f:
            key = json.loads(f.read())
            key['pk'][0] = deserialize_mat(key['pk'][0])
            key['pk'][1] = deserialize_mat(key['pk'][1])
            key['sk'] = deserialize_mat(key['sk'])
    except IOError as e:
        assert e.strerror == 'No such file or directory'
        key = MultiBitKeyGen(800)
        with open("lpn.key", "w") as f:
            f.write(serialize_key(key))     # That will contain serialized version of public key and secret key on server.
    #print key
    ctxt = MultiBitEnc(key['pk'], bytes(codec.encode(m)))   
    #print ctxt
    ptxt = codec.decode(bytearray(MultiBitDec(key['sk'], ctxt)))
    #print ptxt
    return (key, ctxt, ptxt)

if __name__ == '__main__':
    #assert get_values("A"*20)[2][:20] == "A"*20
    key, ctxt, ptxt = get_values(flag)
    print("A: %r\nB: %r\nu: %r\nc: %r" % tuple(map(serialize_mat, (key['pk'][0], key['pk'][1], ctxt[0], ctxt[1]))))
