# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.
import pathlib

# input
#go into sub folders
# find jpgs
#print them in a list

folder_path=input("Enter a path: ")
#folder_path=pathlib.Path(r'C:\\Users\\user_name\\Desktop\\pictures\\') # path where I am starting
#print(folder_path)

for filepath in folder_path.iterdir():
    if filepath.is_dir(): # testing if it is a directory
        #print(filepath)

        for folder in filepath.iterdir():
            if folder.suffix == '.PNG':
                print(folder.name)
            if folder.is_dir():
                for subfolder in folder.iterdir():
                    print(subfolder.name)



# this only goes two level down

#in the future when I have time I can