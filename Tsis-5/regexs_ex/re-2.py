# re-2
import re
sample_txt = "abb abbbbb ab"
x = re.findall(r'ab{2,3}' , sample_txt)
print(x)