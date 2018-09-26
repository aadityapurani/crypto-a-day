Mathematics is essential for solving tedious tasks. Here I provide some hacks which are useful because of strength provided by math and algorithm. This post will be continued and content will be added time to time. 

This is the fundamental steps for cryptography and our goal is to be an excellent cryptographer who is able to applying critical thinking skills in solving problems within 40 days. 

# Modulus
Essentially the remainder when you perform an operation using `%` . 
```
>> a = 10
>> b = 2
>> a%b 
0
>> b%a
2
```

This `a%b` essentially works as
```
    5
  ____
 |  10
2|
_|
----------
    0
```
Here, remainder is 0 and quotient is 5. But let's say we go other way around like `b%a` then 10 cannot divide 2. Hence, we always get remainder is 2.

# Congruency
`≅` represents congruency. Question is how will you prove if `a≅b(mod n)` ?
A congruent relation will hold if and only if `(a-b)%n` is equal to 0.

Python code:
```
from fractions import *

print "Your form should be a congurent  b (mod n)"
a = int(raw_input("a: "))
b = int(raw_input("b: "))
n = int(raw_input("n: "))

f = (a-b)%n
if f==0:
	print "Congruence relation holds"
else:
	print "Nope"
```

#  gcd (Greatest common divisor)
Suppose a = 14, b = 20
a can be factorized as 7 x 2
b can be factorized as 5 x 2 x 2

The only common between two factorization is `2`. Hence, gcd is 2

```
from fractions import *
print gcd(14,20)
```

If `gcd(a,b) == 1`, then `a` and `b` are **Relatively Prime**.
If they are **Relatively Prime** then **multiplicative inverse** of “a modulo b” will exist.

# Multiplicative Inverse (Modulo Inverse)
Given two integers, a and n . then `x` is the multiplicative inverse such way that
```
 a x ≡ 1 (mod n) 
```

Approach, is to brute all integer i from 0 to m-1 and then take `(a*n)%i == 1` . One can re-write question as 
` a^-1 mod n`

Python:
```
def modInverse(a, n) : 
    a = a % n; 
    for x in range(1, n) : 
        if ((a * x) % n == 1) : 
            return x 
    return 1
```

Sage Math supports as `inverse_mod(a,n)` inbuilt function.

A much more simpler but same approach. We will supply in form of  `a x ≡ 1(mod n)` if this is 0 then `x` should be our inverse modulo answer. This however does not check bounds and give you a lot of possible solution. But it could be fixed easily however.

```
from fractions import *

# Inputs are in form of A^-1 mod N
# Same implementation can be used in Sage as A.inverse_mod(N)
# This is just to know the calculations of satisfying congruence theorem to find the same.
# Implemented by @aaditya_purani

A = int(raw_input("A: "))
N = int(raw_input("N: "))
iteration = int(raw_input("Iterations: "))
for x in xrange(1, iteration):
    a = x*A
    n = (a-1)%N
    if n==0:
        print "[+] Found "+str(x)
        print str(x)+" X "+str(A)+" congurent 1 (mod "+str(N)+" )"
```

# Euler's Totient Function
It calculates positive integer less than n that are coprimes to n (coprime is same as relatively prime). Hence, gcd should be 1. It is denoted by φ

```
from fractions import *

# Euler Phi is like phi(n) where you input n and it displays all integer < n which are relatively prime to n
# generally it gives the total number of integers < n which are relatively prime

n = int(raw_input("n: "))
list_num = []

for x in xrange(1, n):
	val = gcd(x, n)
	if val == 1:
		list_num.append(x)

print list_num
print "Total : "+str(len(list_num))
```

Property of totient function is it is multiplication `φ(a.b) = φ(a).φ(b)`

# Prime Numbers
The most fundamental piece of information. A prime number has only exactly 2 positive divsiors - 1 and the number itself. 
2,3,5,7, ... are prime number.

1 is neither prime nor composite number




