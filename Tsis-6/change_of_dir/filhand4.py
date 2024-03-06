# filhand4
# Write a Python program to count the number of lines in a text file.
with open('gojo_satoru.txt') as file:
    count = 0
    for i in file:
        count+=1
    print(count)