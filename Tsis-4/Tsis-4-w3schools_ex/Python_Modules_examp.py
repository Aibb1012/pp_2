# Python_Modules_examp
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.
# To create a module just save the code you want in a file with the file extension .py:
# Now we can use the module we just created, by using the import statement:
import mymodule
mymodule.greeting("Jonathan")
# When using a function from a module, use the syntax: 
#     module_name.function_name.
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
import mymodule
a = mymodule.person1["age"]
print(a)
# You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module:
# You can create an alias when you import a module, by using the as keyword:
import mymodule as mx
a = mx.person1["age"]
print(a)

# Built-in Modules
import platform
x = platform.system()
print(x)
# List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x)


# You can choose to import only parts from a module, by using the from keyword.
# Import only the person1 dictionary from the module:
from mymodule import person1
print (person1["age"])
# When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"]