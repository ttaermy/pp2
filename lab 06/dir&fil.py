#1
import os

path = r'C:\Users\tomir\Desktop\pp2'

entries = list(os.scandir(path))

for entry in entries:
    print(entry.name)

for entry in entries:
    if entry.is_dir():
        print(entry.name)

for entry in entries:
    if entry.is_file():
        print(entry.name)


#2
import os

path = "somefile.txt"

if os.path.exists(path):
    print("Exists")

    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

else:
    print("Doesn't exist")


#3
import os

def test_path_details(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")


#4
import os

def count_lines(file_path):
    counter = 0
    with open(file_path, 'r') as file:
        for line in file:
            counter += 1
    return counter


print("Number of lines:", count_lines(r""))


#5
def write_list_to_file(list_items, file_path):
    with open(file_path, mode='w') as file:
        for item in list_items:
            file.write(f"{item}\n")


write_list_to_file([1, 2, 3, 4, 5], './list_elements.txt')


#6
import string

def generate_26_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            pass


generate_26_files()

#7
import shutil

def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)


#8
import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or is not accessible.")