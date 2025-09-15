def print_formatted(number):
    # Find the maximum width required (length of the binary representation of 'number')
    # For example, if number = 17, bin(17) = '0b10001', bin(17)[2:] = '10001', length = 5
    width = len(bin(number)[2:])

    # Loop through all numbers from 1 to 'number' (inclusive)
    for i in range(1, number + 1):
        # Print i in decimal, octal, hexadecimal (uppercase), and binary
        # Each value is right-aligned using rjust(width) so columns line up nicely

        # str(i).rjust(width) → decimal number right aligned
        # oct(i)[2:].rjust(width) → octal (remove '0o' prefix with [2:])
        # hex(i)[2:].upper().rjust(width) → hexadecimal (remove '0x', uppercase letters)
        # bin(i)[2:].rjust(width) → binary (remove '0b')

        print(str(i).rjust(width), 
              oct(i)[2:].rjust(width), 
              hex(i)[2:].upper().rjust(width), 
              bin(i)[2:].rjust(width))


if __name__ == '__main__':
    # Take input number from user
    n = int(input())

    # Call the function with given number
    print_formatted(n)
