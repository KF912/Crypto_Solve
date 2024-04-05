import libnum

p=447685307
q=2037
e=17
c=704796792

n = q*p
s=(q-1)*(p-1)
d = libnum.invmod(e,s)
# libnum.invmod求逆元
m = pow(c, d, n)
# 内置的 pow() 方法
# pow(x, y[, z])
# 函数是计算 x 的 y 次方，如果 z 在存在，则再对结果进行取模，其结果等效于 pow(x,y) %z。
print(m)