# area_trap
import math
h = float(input("Height:"))
b1 = float(input("Base, first value:"))
b2 =float(input("Base, second value:"))
a = b1+b2
z = 0.5
k = [h , a , z]
print("Expected Output:",math.prod(k))
