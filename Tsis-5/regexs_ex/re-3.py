# re-3
# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re 
sample_txt ='a_s as_aa  aa_b a_ddd'
pt = r'[a-z]+_[a-z]+'
x = re.findall(pt , sample_txt)
print(x)