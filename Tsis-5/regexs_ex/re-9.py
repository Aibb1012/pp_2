#  re-9
# Write a Python program to insert spaces between words starting with capital letters.
import re
sample_txt = "AAbbbAAAccC"
x  = re.sub(r'([A-Z][a-z]+)', r' \1', sample_txt).strip()
print(x)