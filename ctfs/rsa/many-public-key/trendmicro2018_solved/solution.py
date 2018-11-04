# found factors with https://www.numberempire.com/numberfactorizer.php 

from gmpy import *

def text2int(text):
    chars = [ord(c) for c in text]
    result  = 0
    for c in chars:
        result *= 256
        result += c
    return result

def int2text(message):
    result=""
    while message>0:
        result = chr(int(message)%int(256))+ result
        message=int(message)/int(256)
    return result

def encrypt(text, e, N):
    text_int = text2int(text)
    encrypted = pow(text_int, e, N)
    return encrypted

def decrypt(x_int, d, N):
    decrypted = pow(x_int, d, N)
    text = int2text(decrypted)
    return text

e  =  65537

A_m = 18700320110367574655449823553009212724937318442101140581378358928204994827498139841897479168675123789374462637095265564472109735802305521045676412446455683615469865332270051569768255072111079626023422
A_n = 23795719145225386804055015945976331504878851440464956768596487167710701468817080174616923533397144140667518414516928416724767417895751634838329442802874972281385084714429143592029962130216053890866347

B_m = 27979368157170890767030069060194038526134599497456846620984054211906413024410400026053694007247773572972357106574636186987337336771777265971389911503143036021889778839064900818858188026318442675667707
B_n = 46914096084767238967814493997294740286838053572386502727910903794939283633197997427383196569296188299557978279732421725469482678512672280108542428152186999218210536447287087212703368704976239539968977

C_m = 24084879450015204136831744759734371350696278325227327049743434712309456808867398488915798176282769616955247276506807739249439515225213919008982824219656080794207250454008942016125074768497986930713993
C_n = 24543003393712692769038137223030855401835344295968717177380639898023646407807465197761211529143336105057325706788229129519925129413109571220297378014990693203802558792781281981621549760273376606206491

def common_factor_factorization(ns):
    """
    Try to factor given list of moduli by calculating gcd for each pair, hoping that some share the same prime
    :param ns: list of moduli
    :return: list of triplets (modulus1, modulus2, shared prime)
    """
    from itertools import combinations
    return [(n1, n2, gcd(n1, n2)) for n1, n2 in combinations(ns, 2) if gcd(n1, n2) != 1]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


nl = [A_n,B_n,C_n]
cl = [A_m,B_m,C_m]
for na,nb,p in common_factor_factorization(nl):
    i_a = nl.index(na)
    i_b = nl.index(nb)
    q_a = na/p
    phi_a = (p-1)*(q_a-1)
    q_b = nb/p
    phi_b = (p-1)*(q_b-1)
    d_a = modinv(e,phi_a)
    d_b = modinv(e,phi_b)
    ct_a = cl[i_a]
    ct_b = cl[i_a]

    print('a: ' + decrypt(ct_a,d_a,na))
    print('b: ' + decrypt(ct_b,d_b,nb))
    


# approaches 
# 1) find all the factors of the n's and the potential p & q (or p_i's)
# problem n is too big
# 2) CRA?  
# problme nope need to have similar n's and different e's
# 3) find gcd until you run out of factors so you can have all the factors
# they only have 


