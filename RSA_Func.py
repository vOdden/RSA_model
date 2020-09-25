# Python file containing functions for RSA algorithm


#GCD
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
#GCD iteration method
def gcd_iter(a,b):
    while b!= 0:
        (a,b) = (b,a % b)
    return a


def coprime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False

#   https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None


def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r


