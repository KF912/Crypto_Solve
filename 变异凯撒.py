text = 'afZ_r9VYfScOeO_UL^RWUc'
# 偏移量为五
j = 5
for i in text:
    print(chr(ord(i) + j), end='')
    j += 1