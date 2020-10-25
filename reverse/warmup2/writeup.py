


f1 = open('flag.rer','rb')
f2 = open('result','wb')

len_ext = f1.read(1)
ext = f1.read(int.from_bytes(len_ext,byteorder='big'))
key = 'flag.'+ext.decode()
print(key)

while(True):
    b = f1.read(1)
    if not b:
        break
    if int.from_bytes(b,byteorder='big') == 255:
        length = f1.read(1)
        encrypted_bytes = f1.read(int.from_bytes(length,byteorder='big'))
        decrypted_bytes = bytearray()
        for i in range(0,len(encrypted_bytes)):
            decrypted_bytes.append(encrypted_bytes[i] ^ ord(key[i%len(key)]))
        f2.write(decrypted_bytes)
    else:
        length = b
        s = f1.read(1)
        for i in range(0,int.from_bytes(length,byteorder='big')):
            f2.write(s)

f1.close()
f2.close()

