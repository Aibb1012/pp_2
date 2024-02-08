# Factorial
def calculate_factorial(n):
    if n==0:
        return 1
    return n*calculate_factorial(n-1)

a = int(input())
print(calculate_factorial(a))