# file_gengerator26
for letter in range(ord('A'), ord('Z') + 1):
    filename = chr(letter) + ".txt"
    with open(filename, 'w') as file:
        file.write(f"This is the content of file {filename}.")
        print(f"File '{filename}' created successfully.")


