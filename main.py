from sympy import *
# Functions
from RSA_Func import *

#p = int(input("Enter prime number for p:"))
#q = int(input("Enter prime number for q:"))
#m = int(input("Enter message for m:"))
print("--- Configuration ---\n")


p = 7
q = 17
m = 119
pp = isprime(p)
qq = isprime(q)
if(pp and qq):
    print("p and q is prime")
else:
    print("p and q is not prime")
#   Computing  n = pq

n=p*q
print("n =", n)

#   Least common multiple:
phi = (p-1)*(q-1)
print("phi =",phi)

#   Determining e
#   Any prime between 1 < e < phi

for e in range(2,phi-1):
    if gcd_iter(e,phi) == 1:
        break

#   Testing if e and phi is co prime
#   Return true if co prime, otherwise return false
e_1 = coprime(phi,e)
print("Co_Prime test: ",e_1)
#e = 103
print("E =",e)


# d = e^-1 mod phi :  d = 1/e mod phi

d = modinv(e,phi)


#d = mod_inverse(e,phi)
#d = pow(e,p,phi)
print("d =", d)


print("--- Keys ---\n")

# Keys
print("Public key:",e,n)
print("Private key:",d,n,"\n")

print("--- Encrypt/Decrypt ---")
print("Message sent m:",m)


#   Encryption and decryption

#
#Encrypt = pow(m,e,n)
Encrypt = fast_exp(m,e,n)
#Encrypt = (m**e)%n
print("encrypt msg",Encrypt)

Decrypt = (Encrypt**d)%n
print("decrypted msg ",Decrypt)





