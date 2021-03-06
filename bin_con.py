# Bits and lists:
bits_list = []
binary_list = []
result_list = []
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

# Measure for checks.
count_bin = len(str(binary))

if bit_input > count_bin or bit_input < count_bin:
    print("Expected bits: " + str(count_bin) + ", input was " + str(count_bin))
    print("Please adjust binary to " + str(count_bin) + " bits")

# Create bit instances.
while count_bin > 0:
    bits_list.append(bit_add)
    bit_add = bit_add * 2
    count_bin = count_bin - 1

# Sort binary into list, and reverse bits to match.
for var in str(binary):
    binary_list.append(int(var))
bits_list.reverse()

# Calc number off of binary.
pos_var = 0
while pos_var < len(bits_list):
    result_list.append(bits_list[pos_var] * binary_list[pos_var])
    pos_var = pos_var + 1
result = sum(result_list)
    
# Show result.
print(result)
