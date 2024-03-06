# builtinn2
# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def upper_n_lower(q):
    lowercs = 0
    uppercs = 0
    for i in q:
        if i.isalpha():
            if i.isupper():
                uppercs +=1
            if i.islower():
                lowercs+=1
    return f"LowerCase = {lowercs}\nUpperCase = {uppercs}"
myquote = "In all the heavens and the earth, I Alone Am The Honored One"
print(upper_n_lower(myquote))