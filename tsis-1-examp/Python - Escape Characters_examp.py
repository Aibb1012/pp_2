# Python - Escape Characters

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

# The escape character allows you to use double quotes when you normally would not be allowed:
# to fix problem , use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."

# \'	Single Quote:
txt = 'It\'s alright.'
print(txt) 

# \\	Backslash:
txt = "This will insert one \\ (backslash)."
print(txt) 

# \n	New Line:
txt = "Hello\nWorld!"
print(txt) 

# \r	Carriage Return
txt = "Hello\rWorld!"
print(txt) 

# \t	Tab
txt = "Hello\tWorld!"
print(txt) 

# \b	Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

# \ooo	Octal value
txt = "\110\145\154\154\157"
print(txt) 

# \xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

