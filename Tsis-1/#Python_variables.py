#Python variables
carname = "Volvo"
x=50

x=5
y=10
#print(x+y)
z = x + y
print(z)
x , y ,z ="Orange", "Banana" , "Cherry"
x = y = z = "Orange"

#Insert the correct keyword to make the variable x belong to the global scope
def myfunc():
    global x
    x = "fantastic"