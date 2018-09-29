def pkcs7pad(s, l):
    return s.ljust(l, chr(l-len(s)))
