# filhand2
# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
mypath = r'C:\Users\acer\Documents\pp2_springg\Tsis-4'
import os 

# Check access with os.F_OK 
path1 = os.access(mypath, os.F_OK) 
print("Does the path exists:", path1) 

# Check access with os.R_OK 
path2 = os.access(mypath, os.R_OK) 
print("Access to read the file:", path2) 

# Check access with os.W_OK 
path3 = os.access(mypath, os.W_OK) 
print("Access to write to file:", path3) 

# Check access with os.X_OK 
path4 = os.access(mypath, os.X_OK) 
print("Can path be executed:", path4)
