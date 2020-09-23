# Python file containing functions for RSA algorithm
import random

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def coprime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False


