#Python_strings
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]
#print(x)

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip() #function that deletes whutespace at the beginning or the end
#print(x)

txt = "Hello World"
txt = txt.upper()
#print(txt)

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H" , "J")
#print(txt)

age = 36
txt = "My name is John , and I am {}"
print(txt.format(age))