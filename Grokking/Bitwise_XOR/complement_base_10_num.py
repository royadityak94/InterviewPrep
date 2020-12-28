# Python program to compute the complement of base 10 number
def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def calculate_bitwise_complement(num):
    # Time Complexity = O(N), Space Complexity = O(1)
    required_bits, n = 0, num
    while n > 0:
        n = n >> 1
        required_bits += 1

    # Alternate way:
    #required_bits = len('{:b}'.format(n))

    all_bits_set = (2**required_bits) - 1
    return num ^ all_bits_set

def main():
    test(7, calculate_bitwise_complement(8), "Test for Decimal value of 8")
    test(5, calculate_bitwise_complement(10), "Test for Decimal value of 10")

main()
