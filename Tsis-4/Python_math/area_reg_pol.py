# area_reg_pol
import math
n = float(input("Input number of sides:"))
l = float(input("Input the length of a side:"))
area = n*(l**2)/(4*math.tan(math.pi/n))
print("The area of polygon is:" , area)