from sympy import *
# Functions
from RSA_Func import *

#p = int(input("Enter prime number for p:"))
#q = int(input("Enter prime number for q:"))
#m = int(input("Enter message for m:"))

p = 7 # 7
q = 17 # 17
m = 3

#   Computing  n = pq
n=p*q
print("n =", n)

# Least common multiple:
phi = (p-1)*(q-1)
print("phi =",phi)


# Any prime between 1 < e < phi
minPrime = 0
maxPrime = 2000
prime_list = [i for i in range(minPrime,maxPrime) if isprime(i)]
e = random.choice([i for i in prime_list if 2<i<phi])

e_1 = coprime(phi,e) #coprime check
print("Coprime test: ",e_1)
#e = 103
print("E =",e)



d = mod_inverse(e,phi)
#d = pow(e,p,phi)
print("d =", d)



# Keys
print("Public key:",e,n)
print("Private key:",d,n)

print("-----\nMessage sent m:",m)


#   Encryption and decryption
Encrypt = (m**e)%n
print("encrypt msg",Encrypt)

Decrypt = (Encrypt**d)%n
print("decrypted msg ",Decrypt)


