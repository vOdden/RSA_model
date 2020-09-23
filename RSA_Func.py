# Python file containing functions for RSA algorithm
import random

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def coprime(a, b):
    if gcd(a, b) == 1:
        return b
    # coprime(a,b+1)


