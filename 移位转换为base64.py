# flag使用base64加密后的字符串是 ZmxhZw==
# 前面的ZmxhZ不管flag后面是什么都不会改变。
# 我们对比一下前四个字符，"Zmxh"和"3EP/"在base64表中查一下，Z和3差了30，m和E差了30。
# 将3EP/3VNFFmNEAnlHD5dCMmVHD5ad9uG 在ascii码中向后减30

s= '3EP/3VNFFmNEAnlHD5dCMmVHD5ad9uG'
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
l=""

for i in s:
    l += t[(t.index(i)-30)%64]

if len(l)%4!=0:
    l=l+"="*(4-(len(l)%4))
    print(l)

import base64
print(base64.b64decode(l).decode())