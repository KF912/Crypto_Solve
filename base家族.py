import string
import base64
with open('d:\Desktop\CyberSecurtiy\CTF\ctfshow crypto\problem\\base.txt') as f:
    text = f.read()
while(1):
    try:
        text = base64.b64decode(text).decode()
    except Exception as e:
        try:
            text = base64.b32decode(text).decode()
        except Exception as e:
            try:
                text = base64.b16decode(text).decode()
            except Exception as e:
                break
print(text)