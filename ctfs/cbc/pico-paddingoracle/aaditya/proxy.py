#!/usr/bin/python

# Because none of padbuster implementation works without HTTP

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    from pwn import remote

    c = request.cookies.get("c")
    print `c`

    r = remote('2018shell3.picoctf.com', port)
    r.readuntil('cookie?')
    r.writeline(c)
    d = r.readline()
    d = r.readline()
    r.close()
    print `d`
    if 'invalid padding' in d:
        return 'padding', 500

    return d, 200

if __name__ == '__main__':
    app.run()
