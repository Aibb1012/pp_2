# is_palindrome
s = input()
def is_palindrome():
    x = s[::-1]
    if x == s:
        return True
    else: return False
print(is_palindrome())