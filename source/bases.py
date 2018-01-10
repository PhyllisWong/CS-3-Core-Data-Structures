#!python

import string

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digits_length = len(digits)
    total = 0

    for i in range(digits_length):
        # pow(b, i) uses the formula b^i
        # string.printable.index(digits[i].lower()) searches for the element, and returns the position in a list
        # iterate from the right to left
        total += string.printable.index(digits[i].lower()) * pow(base, digits_length -i -1)
    print(total)
    return int(total)


def encode(number, base):
    """Encode given number in base10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    max_value = 0
    digit_index = 0
    encoded_str = ''

    # while the number is still divisible
    while max_value <= number:
        # Set max_value as base to the power of the digit's position
        max_value = pow(base, digit_index)
        digit_index += 1
    # Remove the digit we added before the check / subtract another because we check against the max
    digit_index -= 2

    # Iterate from right to left through the index positions
    for i in range(digit_index, -1, -1):
        # The power of the index. Ex: b^i
        power = pow(base, i)
        # If number is greater than the value of power at the current index,
        # continue by getting the character we need and adding it.
        # If number is lower the value of power at the current index, add a 0.
        if number - power >= 0:
            remainder = power % number

            if remainder < 1:
                num_times = 1
            else:
                num_times = int(number/power)

            encoded_str += string.printable[num_times]
            number -= (power * num_times)
        else:
            encoded_str += '0'
    return encoded_str


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Convert digits from base2 to base16 (and vice versa)
    # Decode converts digits in any base from 2 to 36  to base10
    decoded = decode(digits, base1)
    # Encode converts digits from base10 to any base 2 to 36.
    encoded = encode(decoded, base2)
    return encoded


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':

    main()
