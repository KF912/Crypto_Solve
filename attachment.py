# import gmpy2
# from Crypto.Util.number import *
# from binascii import a2b_hex,b2a_hex
#
# flag = "*****************"
#
# p = 262248800182277040650192055439906580479
# q = 262854994239322828547925595487519915551
#
# e = 65533
# n = p*q
#
#
# c = pow(int(b2a_hex(flag),16),e,n)
#
# print c

# 27565231154623519221597938803435789010285480123476977081867877272451638645710


# 首先，我们审计题目，可以得知题目中的p，q，e，n，以及c值，那么需要我们去求解m值，可以发现此题为rsa基础题。

#我们知道m=gmpy2.powmod(c,d,phi_n)，于是，在此题中，我们通过已知的条件求出phi_n和d即可。

# 所以，我们不妨写出一下脚本：

import gmpy2

from Crypto.Util.number import *

from binascii import a2b_hex,b2a_hex

p = 262248800182277040650192055439906580479

q = 262854994239322828547925595487519915551

e = 65533

n = p*q

c=27565231154623519221597938803435789010285480123476977081867877272451638645710

phi=(p-1)*(q-1)

d=gmpy2.invert(e,phi)

m=gmpy2.powmod(c,d,n)

print(long_to_bytes(m))
