# re-6
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
sample_txt = "Throughout heavens and Earth , I.Alone am.The honoured one"
x = sample_txt
x = re.sub('\s' , ':' ,x)  
x = re.sub(',' , ':' ,x)
x = re.sub('[.]' , ':' ,x)
print(x)