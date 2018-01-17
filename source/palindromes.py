#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    clean_text = remove_punctuation(text)
    # return is_palindrome_iterative(clean_text)
    return is_palindrome_recursive(clean_text)


def remove_punctuation(text):
    """Clean the text before checking if it reads the same forwards and backwards."""
    no_punc = ''
    text = text.lower()
    for char in text:
        if char in string.ascii_lowercase:
            no_punc += char
    # print(no_punc)
    return no_punc


def is_palindrome_iterative(text):
    left = 0
    right = len(text)-1

    while right - left > 0:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(text) -1

    if len(text) <= 1 or text == '':
        return True

    if right - left < 1:
        return True

    while left <= right:
        if text[left] == text[right]:
            return is_palindrome_recursive(text, left +1, right -1)
        return False
    return True



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


def test_is_palindrome(text):
    """A function to test if the iterative and recursive palindrome functions
    are working as expected."""
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    clean_text = remove_punctuation(text)
    print(is_palindrome_iterative(clean_text))
    # return is_palindrome_recursive(clean_text)


if __name__ == '__main__':
    # test = is_palindrome_iterative('dog god?')
    # print("Func call: {}".format(test))
    main()
