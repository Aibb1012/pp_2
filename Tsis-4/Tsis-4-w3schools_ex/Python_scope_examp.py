# Python_scope_examp
# A variable is only available from inside the region it is created. This is called scope.

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = 300
  print(x)

myfunc()

# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# A variable created outside of a function is global and can be used by anyone:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# The function will print the local x, and then the code will print the global x:
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()

print(x)

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
def myfunc():
  global x
  x = 300

myfunc()

print(x)
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)


