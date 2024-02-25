# re-8
# Write a Python program to split a string at uppercase letters.
import re 
sample_txt = "areYouNahIdWinBecauseYour TheHonoredOne"
x = re.split('[A-Z]' , sample_txt)
print(x)