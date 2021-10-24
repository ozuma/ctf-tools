#!/usr/bin/python3 
 
from Crypto.Util.number import getPrime, inverse 
import binascii 
 
# 2つの素数 
# ここで素因数分解： https://www.alpertron.com.ar/ECM.HTM 
p = 1899107986527483535344517113948531328331 
q = 674357869540600933870145899564746495319033 
 
# Modulus n = p * q 
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923 
 
# Public Exponent 
e = 65537 
 
# EncyptData 
c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021 
 
phi = (p-1)*(q-1) 
 
# Private Exponent 
d = inverse(e, phi) 
 
# Decrypt! 
m = pow(c, d, n) 
print repr(binascii.unhexlify(hex(m)[2:-1])) 

