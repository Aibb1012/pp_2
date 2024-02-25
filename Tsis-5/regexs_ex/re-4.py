# re-4
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re 
sample_txt ='Aab aaA BBa Av Akk'
pt = r'([A-Z][a-z]+)+'
x = re.findall(pt , sample_txt)
print(x)