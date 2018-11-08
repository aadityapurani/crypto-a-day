from Crypto.Util.number import *
from gmpy import *
import math
import os
import sys
sys.path.append(os.getcwd()+'/etc')
import get_list_of_primes
primes = get_list_of_primes.primes[:60000]
# for num in range(2,100000000):
#     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#        primes.append(num)
#get a list of primes

#git message from the system twice
# m1 = 'ab'
# c1 = '22ba1d44e7d96e185292bf56de7ddf91cb10dffdf98725c0cc699ecc78096258e5a09ce67927f7aabd32274453ca5d25af41d767ff434cfa013aa56f207815174e6cca65580b7fdac59ea32f5ae05e9158f93de999b6922b476aa55e2f81e657a14efaa507a539d290134695e75c1f109776b4d06196131789934869f0fd6805'.decode('hex')
# m2 = 'cd'
# c2 = '3107b72dd83b8ad0e6d15244f0a843c2b40e5a3913ff5cd3bb602f11a70ab211ce844a43d1168ca75bede76bf4e4bd94beca7188a4f7052fe6c0e31af29ad055e099806a20a546fe060b536f13196660771c79cb68c810d593b354f92763562dcb82dc0586b97eaedc40a84247c066642f4e526810b1b1c12e1e1355c98bb17d'.decode('hex')

# #convert to useable form
# m1 = bytes_to_long(m1)
# c1 = bytes_to_long(c1)
# m2 = bytes_to_long(m2)
# c2 = bytes_to_long(c2)

# def calc(cipher_text,message,e):
#     return pow(message,e)-cipher_text


# def main():
#     #choose from primes
#     for pot_e in primes:
