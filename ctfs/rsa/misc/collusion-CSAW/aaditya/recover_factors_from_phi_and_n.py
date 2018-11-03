# https://groups.google.com/forum/#!topic/sci.crypt/wDV49EsAZQ0

def gcd(x, y):
    """Return the GCD of x and y."""
    while x>0:
        x, y = y%x, x
    return y

def split_using_lambda(n, s):
    """Given a composite n and and a multiple of lambda(n),
    return a non-trival factor of n.
    Loops out or asserts false on bad inputs.
    """
    #  Divide factors of 2 out of exponent s
    while s & 1 == 0:
        s = s >> 1
    #  Try bases until we find a factor
    for base in xrange(1, 999, 2):
        #  Realy we should set base randomly, but this works
        a = pow(long(base), s, n)
        if a == 1:
            #  Darn, we got to 1 without finding a square root
            continue
        #  Keep squaring until we hit 1.
        while a != 1 and a != n-1:
            b = a
            a = a * a % n
        if a == 1:
            #  Got it
            return gcd(n, b + 1)
        # Darn, the square root we found was -1.
    assert(0), "Something is very wrong."
