# How many bits:
bits = 6
bits_list = []
bit_add = 1

# Def the below once this works.
while bits > 0:
    bits_list.append(bit_add)
    bit_add = bit_add * 2
    bits = bits - 1

print(bits_list)

binary = input("Input binary up to " + str(bits) + " bits: ")
binary = str(binary)
print(binary)
