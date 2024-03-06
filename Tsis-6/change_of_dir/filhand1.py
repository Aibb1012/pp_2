# filhand1
import os

def list_directories_and_files(path):
    print("Only directories:")
    directories = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            directories.append(name)
    print(directories)

    print("\nOnly files:")
    files = []
    for name in os.listdir(path):
        if not os.path.isdir(os.path.join(path, name)):
            files.append(name)
    print(files)

    print("\nAll directories and files:")
    all_items = []
    for name in os.listdir(path):
        all_items.append(name)
    print(all_items)

# Example usage:
specified_path = r'C:\Users\acer\Documents\pp2_springg\Tsis-4'
list_directories_and_files(specified_path)