def is_palindrome(x):
    """
    SIMPLE O(n) Solution:

    number = str(x)
    if number == number[::-1]:
        return True
    else:
        return False
    if x < 0:
        return False
    """

    # O(log10(n)) Solution - Optimised and without using built-in functions
    original_x = x
    reverse_x = 0
    while x > 0:
        digit = x % 10
        reverse_x = reverse_x * 10 + digit
        x //= 10

    return original_x == reverse_x


print(is_palindrome(121))
