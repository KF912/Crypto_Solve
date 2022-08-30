# c22a563acc2a587afbfaaaa6d67bc6e628872b00bd7e998873881f7c6fdc62fc
import hashlib
count = 0
string = 'c22a563acc2a587afbfaaaa6d67bc6e628872b00bd7e998873881f7c6fdc62fc'
data = "8617090000000"   # 要进行加密的数据

data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()  

while string != data_sha :
    count= count + 1
    data = int(data)+1
    data = str(data)
    data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()   
    print(data)
    print(data_sha)



print(count)
print(data)
print(data_sha)