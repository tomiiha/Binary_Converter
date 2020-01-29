# How many bits.
bits_list = []
binary_list = []
bit_add = 1

# User bits input.
while True:
    try:
        bit_input = input("Input total bits: ")
        bit_input = int(bit_input)
        break
    except ValueError:
        print("Input a number.")
        continue
    
# User binary input.
while True:
    try:
        binary = input("Input binary up to " + str(bit_input) + " bits: ")
        binary = int(binary)
        break
    except ValueError:
        print("Input only 1s and 0s.")
        continue

# Convert that to something we can measure in length.
count_bin = len(str(binary))

if bit_input > count_bin or bit_input < count_bin:
    print("Expected bits: " + str(count_bin) + ", input was " + str(count_bin))
    print("Please adjust binary to " + str(count_bin) + " bits")

# Create bit instances.
while count_bin > 0:
    bits_list.append(bit_add)
    bit_add = bit_add * 2
    count_bin = count_bin - 1

# Sort binary into list.
for var in str(binary):
    binary_list.append(var)

# Reverse to assign bit ordering.
bits_list.reverse()

# Show bit numbers
print(bits_list)
print(binary_list)
