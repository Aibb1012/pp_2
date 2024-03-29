# Python Booleans_examp
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Functions can return a boolean
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

