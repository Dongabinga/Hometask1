def is_palindrome(n):
    if isinstance(n, int):
        n = str(n)
    return n == n[::-1]
result = is_palindrome(123)
print(result)
