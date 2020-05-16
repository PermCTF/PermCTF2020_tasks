import matplotlib.pyplot as plt
import numpy as np

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

flag = "PermCTF{Tru3_1if3_m0d3l}"
A1 = 0.004
A2 = A1/2
step = 0.01
dot_size = 0.1
dot_color = "Black"
dt = 4*np.pi

# Convert text to the binary code
binary = text_to_bits(flag)
print(binary)
s1, s2 = [],[]

# Hard to explain what's going on here
# Assing time range depending on current bit value
for pos,val in enumerate(binary):
    if val == '1':
        s1 = s1 + list(np.arange(pos*dt, (pos+1)*dt, step))
    else:
        s2 = s2 + list(np.arange(pos*dt, (pos+1)*dt, step))

# Create a high amplitude sin
signal = A1*np.sin(s1)
plt.scatter(s1, signal, s = dot_size, color = dot_color)

# Create a low amplitude sin
signal = A2*np.sin(s2)
plt.scatter(s2, signal, s = dot_size, color = dot_color)

#plt.savefig("signal.png", dpi=2100)
plt.show()
