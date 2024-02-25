# re-5
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re 
sample_txt ='acccb, svvvcb ,saVVobb'
pt = r'(a.*b$)+'
x = re.findall(pt , sample_txt)
print(x)