import sys
from fractions import *

# Automation for DH Worksheet Cornell Crypto course
# https://www.math.cornell.edu/~mec/2003-2004/cryptography/diffiehellman/worksheet.html
# No use of Sage and crypto library, keeping it simple

# Modulus P should be prime
P = 257
# Primitive root N
N = 3

# Factors calculating function
def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

# Secret Exponent
A = 113

# Calculating common factors based on secret exponent
commonf = gcd(A, P-1)

if commonf == 1:
	print "This Secret exponent would work fine"
else:
	print "Common factor exists. Recommend changing"

# Repeating Square Method

n  = N%P
n2 = pow(N,2)%P
n4 = pow(N,4)%P
n8 = pow(N,8)%P
n16 = pow(N,16)%P
n32 = pow(N,32)%P
n64 = pow(N,64)%P
n128 = pow(N,128)%P

# A can be broken as 113 = 64+32+16+1
# The number you will send to Bob would be J
# Calculated as J = N^E(mod P)
J = (n64*n32*n16*n)%P

# Partner's Private key woyld be E1 which they won't share
B = 53

# They will calculate K and send to you
K = (n32*n16*n4*n)%P

# You will again use repeated Squaring Method
k = K%P
k2 = pow(K,2)%P
k4 = pow(K,4)%P
k8 = pow(K,8)%P
k16 = pow(K,16)%P
k32= pow(K,32)%P
k64 =pow(K,64)%P
k128 =pow(K,128)%P

# Calculate Shared Secret of yours
your_shareds = (k64*k32*k16*k)%P

# They will use yours 
j = J%P
j2 = pow(J,2)%P
j4 = pow(J,4)%P
j8 = pow(J,8)%P
j16 = pow(J,16)%P
j32 = pow(J,32)%P

their_shareds = (j32*j16*j4*j)%P

print "Your Shared Secret: "+str(your_shareds)
print "\nTheir Shared Secret: "+str(their_shareds)

if your_shareds == their_shareds:
	print "\n[+] Successful Diffie Hellman Exchange"
else:
	print "\n[-] Go Home, your'e drunk!"
