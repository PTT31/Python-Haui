import os
os.chdir(r'F:/python/txtvless')
vless="vless://26ad61cb-9e0c-4d19-e8a1-5f385e8a80b5@20.247.88.38:80?type=ws&security=none&path=%2F&host="
f = open ("domain.txt", mode = 'r', encoding = 'utf-8')
f2 =  open ("vless.txt", mode = 'w', encoding = 'utf-8')
#raw = f.read()
#read = list(raw.split('\n'))
#print(vless + read[0])
while True:
    read = f.readline()
    if read == '':
        break
    f2.write(vless + read)
f2.close()
f.close()
