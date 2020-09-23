from sympy import *
# Functions
from RSA_Func import *

p = int(input("Enter prime number for p:"))
q = int(input("Enter prime number for q:"))
m = int(input("Enter message for m:"))
print("--- Configuration ---\n")
#p = 17
#q = 41
#m = 600

#   Computing  n = pq
n=p*q
print("n =", n)

#   Least common multiple:
phi = (p-1)*(q-1)
print("phi =",phi)


#   Any prime between 1 < e < phi

for e in range(2,phi):
    if gcd(e,phi) == 1:
        break

e_1 = coprime(phi,e)
print("Coprime test: ",e_1)
#e = 103
print("E =",e)



d = mod_inverse(e,phi)
#d = pow(e,p,phi)
print("d =", d)


print("--- Keys ---\n")

# Keys
print("Public key:",e,n)
print("Private key:",d,n)

print("--- Encrypt/Decrypt ---\n")
print("Message sent m:",m)


#   Encryption and decryption
Encrypt = (m**e)%n
print("encrypt msg",Encrypt)

Decrypt = (Encrypt**d)%n
print("decrypted msg ",Decrypt)


