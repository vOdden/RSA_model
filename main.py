from sympy import *
# Functions
from RSA_Func import *

#p = int(input("Enter prime number for p:"))
#q = int(input("Enter prime number for q:"))
#m = int(input("Enter message for m:"))

print("--- Configuration ---\n")
# -- Configuration of p,q,m --
p = 7
q = 17
m = 119
pp = isprime(p)
qq = isprime(q)
# Testing if p and q equals a prime number.
if(pp and qq):
    print("p and q is prime")
else:
    print("p and q is not prime")

#   Computing  n = pq
n=p*q
print("n =", n)

# Finding the least common multiple(LCM):
phi = (p-1)*(q-1)
print("phi =",phi)

#   Determining e
#   any prime number between 1 < e < phi

for e in range(2,phi-1):
    if gcd_iter(e,phi) == 1:
        break

#   Testing if e and phi is relative prime
#   Return true if relative prime, otherwise return false
e_1 = coprime(phi,e)
print("Co_Prime test: ",e_1)
print("e =",e)


#   Calculating the modular mutliplicative inverse
d = modinv(e,phi)

print("d =", d)

print("--- Keys ---\n")

# Keys
print("Public key:",e,n)
print("Private key:",d,n,"\n")

print("--- Encrypt/Decrypt ---")
print("Message sent m:",m)


#   Encryption and decryption

#Encrypt = pow(m,e,n) || Another way to calculate encrypt
Encrypt = fast_exp(m,e,n)
#Encrypt = (m**e)%n
print("encrypt msg",Encrypt)

Decrypt = (Encrypt**d)%n
print("decrypted msg ",Decrypt)





