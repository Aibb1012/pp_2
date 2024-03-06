# filhand5
# Write a Python program to write a list to a file.
# import os
with open('yuta_okotsu.txt' , 'w') as file:
    given_list = ['Are you Gojo Satoru' , 'Because you are the strongest?' , 11 , 'Or you are the strongest' , 'Because youre Gojo Satoru']
    for i in given_list:
        file.write(str(i) + '\n')

g = open('yuta_okotsu.txt' , 'r')
print(g.read())