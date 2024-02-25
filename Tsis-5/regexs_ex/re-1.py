# re-1

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
sample_txt = "ccabbbb ab abb"

x = re.findall(r'(ab*$)+', sample_txt)
print(x)