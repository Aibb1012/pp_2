# filhand3
# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
mypath = r'C:\Users\acer\Documents\pp2_springg\Tsis-4\iterators_generators'
if os.path.exists(mypath):
    print("Yes")
    files = os.path.split(mypath)
    print(files[0])
    print(files[1])
else:
    print("This path does not exist")