# How many bits:
bits = 6
bits_list = []
bit_add = 1

# User binary input.
while True:
    try:
        binary = input("Input binary up to " + str(bits) + " bits: ")
        int(binary)
        break
    except ValueError:
        print("Input only 1s and 0s.")
        continue

# Convert that to something we can measure in length.
binary = str(binary)
count_bin = len(binary)

if bits > count_bin or bits < count_bin:
    print("Expected bits: " + str(bits) + ", input was " + str(count_bin))
    print("Please adjust binary to " + str(count_bin) + " bits")

while bits > 0:
    bits_list.append(bit_add)
    bit_add = bit_add * 2
    bits = bits - 1
