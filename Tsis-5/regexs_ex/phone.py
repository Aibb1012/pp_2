# phone
import re 

pt = r"^(?:\+7|8)(?:(705)|(777)|(771))[0-9]{7}$"
sample_tx = "+77051234567"
s2 = "87710501"
s3 = "97770101560"
print(bool(re.match(pt , sample_tx)))
print(bool(re.match(pt , s2)))
print(bool(re.match(pt , s3)))