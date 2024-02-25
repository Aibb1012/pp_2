# re-10
# Write a Python program to convert a given camel case string to snake case.
import re
sample_txt = "CamelCase TuringMachine"
x = re.sub('([a-z0-9])([A-Z])', r'\1_\2', sample_txt).lower()
print(x)