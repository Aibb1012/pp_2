# re-7
# Write a python program to convert snake case string to camel case string.
import re

def snake_to_camel(word):
    # Replace underscores with spaces, capitalize each word, and remove spaces
    def capitalize(match):
        return match.group(1).upper()

    return re.sub(r'_([a-zA-Z])', capitalize, word)

snake_case_string = input()
camel_case_result = snake_to_camel(snake_case_string)
print(f"Snake case: {snake_case_string}")
print(f"Camel case: {camel_case_result}")
