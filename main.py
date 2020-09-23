import math
from random import *
from sympy import *
# Functions
from RSA_Func import *

#p = int(input("Enter prime number for p:"))
#q = int(input("Enter prime number for q:"))
p = 7 # 7
q = 17 # 17


#   Computing  n = pq
n=p*q
print("n =", n)

# Least common multiple:
phi = (p-1)*(q-1)
print("phi =",phi)


# Any number 1 < e < phi
#e = randint(2,phi-1)
#e = coprime(phi,1)

# Generating random primal numbers between a and b
minPrime = 0
maxPrime = 1000
prime_list = [i for i in range(minPrime,maxPrime) if isprime(i)]
e = random.choice([i for i in prime_list if p<i<q])
#e = 103
print("E =",e)



#d = mod_inverse(e,phi)
d = pow(e,p,phi)
print("d =", d)


#m = int(input("Enter message for m:"))
m = 100
# Keys
print("Public key:",e,n)
print("Private key:",d,n)

print("-----\nMessage sent m:",m)

# Encrypt & Decrypt

#   Encrypt and decrypt
Encrypt = (m**e)%n
print("encrypt msg",Encrypt)

Decrypt = (Encrypt**d)%n
print("decrypted msg ",Decrypt)


