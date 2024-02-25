# _regex1 
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$" , txt)
# The re module offers a set of functions that allows us to search a string for a match:
# findall - 	Returns a list containing all matches
# search - Returns a Match object if there is a match anywhere in the string
# split - Returns a list where the string has been split at each match
# sub - Replaces one or many matches with a string
# [] - A set of characters "[a-m]"
# \ - Signals a special sequence (can also be used to escape special characters) "\d"
# . - Any character (except newline character) "he..o"
# ^ - starts with
# $ - ends with
# * - zero or more occurences "he.*o"
# + - one or more occurrences "he.+o"
# ? - zero or one occurences "he.?o"
# {} - Exactly the specified number of occurrences	"he.{2}o"
# () - capture and group
# | either or "falls|stays"

# \b	Returns a match where the specified characters are at the beginning or at the end of a word   r"\bain"
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")        r"aind\b"
# \B  vice-versa to the \b
# \A Returns a match if the specified characters are at the beginning of the string "\AThe"
# \d - Returns a match where the string contains digits (numbers from 0-9)

# \s - Returns a match where the string contains a white space character
#\S - vice-versa to the \s
# \w - Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

# import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt) #returns an empty list if no match was found
print(x)
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Split at each white-space character:
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt) #The9rain9in9Spain
print(x)

# If there is no match, the value None will be returned, instead of the Match Object.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())