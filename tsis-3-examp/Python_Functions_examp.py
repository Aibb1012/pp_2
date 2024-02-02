# Python_Functions_examp
#creating functions
def my_function():
  print("Hello from a function")
#Calling a function
def my_function():
  print("Hello from a function")
my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
def myfunction():
  pass

# Positional-Only Arguments
def my_function(x, /):
  print(x)
my_function(3)

# But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /):
  print(x)

my_function(x = 3) #error

# Keyword-Only Arguments
def my_function(*, x):
  print(x)
my_function(x = 3)
# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)
my_function(3)

# Combine Positional-Only and Keyword-Only
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

# Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)


