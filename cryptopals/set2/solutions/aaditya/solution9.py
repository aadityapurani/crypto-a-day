def pkcs7pad(s, l):
    return s.ljust(l, chr(l-len(s)))

def pkcs7unpad(s, l):
    if len(s) == l:
        l = ord(s[-1])
        ok = (s[-l:] == s[-1] * l)
        if ok:
            return True, s[:-l]
        else:
            return False, ''
    else:
        return False, ''
