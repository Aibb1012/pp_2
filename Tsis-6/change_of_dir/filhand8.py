# filhand8
# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
if os.path.exists(r'C:\Users\acer\Documents\pp2_springg\Tsis-6\change_of_dir\deletelater.txt'):
    os.remove('deletelater.txt')
else:
    print("There is no file in such directory")