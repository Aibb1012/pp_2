# Python For Loops_examp

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #print each fruit in a fruit list

for x in "banana":
  print(x) #Loop through the letters in the word "banana"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#before the print  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# The continue Statement:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6): #6 is not included
  print(x)

for x in range(2, 6): # start parameter
  print(x)

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else: #The else block will NOT be executed if the loop is stopped by a break statement.
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
