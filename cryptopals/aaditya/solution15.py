# I have already implemented in solution9.py

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
