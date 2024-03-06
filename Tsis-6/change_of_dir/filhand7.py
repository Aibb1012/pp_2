# filhand7
# Write a Python program to copy the contents of a file to another file
with open('gojo_satoru.txt', 'r') as firstfile, open('yuta_okotsu.txt', 'w') as secondfile:
    for line in firstfile:
        secondfile.write(line)