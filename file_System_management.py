import os
import shutil

# reading the folder files

folder_path = r"C:\Users\Abhi\OneDrive\Linux - Resources"
os.chdir(folder_path)
# print(os.getcwd())

# check number of files
os.listdir()

# get extension

list_extension = []

for fl in os.listdir():
    extension = fl.split(".")[-1]
    list_extension.append(extension)

list_extension = set(list_extension)
# print(list_extension)
# print(len(list_extension))

path = os.environ["UserProfile"] + "\\" + "Desktop" + "\\" + "File_Management"

try:
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)

# transfer files

for ex in list_extension:
    print(ex, end=",")
    os.mkdir(path + "\\" + ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl, path + "\\" + ex)
