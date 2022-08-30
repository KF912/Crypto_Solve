# from hashlib import md5
# key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in key:
#     for j in key:
#         for k in key:
#             s = 'TASC'+i+'O3RJMV'+j+'WDJKX'+k+'ZM'
#             m = md5()
#             m.update(s.encode('utf-8'))     #注意转码
#             res = m.hexdigest()
#             if 'e903' in res and '4dab' in res and '08' in res and '51' in res and '80' in res and '8a' in res:
#                 print(res)
#                 break
            

# -*- coding: utf-8 -*-
#!/usr/bin/env python
import hashlib

#print hashlib.md5(s).hexdigest().upper()
k = 'TASC?O3RJMV?WDJKX?ZM'                    #要还原的明文
for i in range(26):
	temp1 = k.replace('?',str(chr(65+i)),1)
	for j in range(26):
		temp2 = temp1.replace('?',chr(65+j),1)
		for n in range(26):
			temp3 = temp2.replace('?',chr(65+n),1)
			s = hashlib.md5(temp3.encode('utf8')).hexdigest().upper()#注意大小写
			if s[:4] == 'E903':    #检查元素
				print (s)       #输出密文
