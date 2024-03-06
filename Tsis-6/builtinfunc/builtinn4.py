# builtinn4
# Write a Python program that invoke square root function after specific milliseconds.
import math
import time
a = float(input())
t = float(input())
time.sleep(t/1000)
result = math.sqrt(a)
print(f"Square root of {a} after {t} miliseconds is {result}")
