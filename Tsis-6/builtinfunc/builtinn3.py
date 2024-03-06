# builtinn3
# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
mystring = "abba"
def ispalindrome(q):
    k = 0
    v = q[::-1]
    if v == q:
        k=1
    return k
# print(bool(ispalindrome(mystring)))
x = ispalindrome(mystring)
print(bool(x))