# builtinn1
# Write a Python program with builtin function to multiply all the numbers in a list
def myfunc(a):
    prod = 1
    for i in a:
        prod*=i
    a.append(prod)
a = [1,2,3,4,5 , 6 , 7]
myfunc(a)
print(max(a))
