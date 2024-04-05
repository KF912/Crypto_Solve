import gmpy2 

p = 447685307 
q = 2037 
e = 17

s = (p-1)*(q-1)
# 求大整数x模m的逆元y
# import gmpy2
# #4*6 ≡ 1 mod 23
# gmpy2.invert(4,23)
# result:mpz(6)
d = gmpy2.invert(e,s)
print ("dec: " + str(d)) 
print ("hex: " + hex(d))