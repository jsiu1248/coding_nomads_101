# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

import pathlib
#desktop=pathlib.Path.home() # how to get the home path
#print(desktop)

new_path=pathlib.Path('C:/Users/jsiu/Desktop/screenshots_folder') # path where I want the pngs to go
new_path.mkdir(exist_ok=True)

#current=pathlib.Path().cwd() # how to get the cwd
#print(current)
print(new_path)

#filter for screenshots meaning move all files with .png

pic_path=pathlib.Path('/Users/jsiu/Pictures') #path of where the pictures are
#iterdir - iterates over the files in directory
for filepath in pic_path.iterdir(): #looking over where the pictures are and iterating over them
    if filepath.suffix =='.png':
        #create a new path for each file
        new_filepath = new_path.joinpath(filepath.name) # concat the names of the path where I want the pngs to go and the names of the pictures
        #move files to new directory
        filepath.replace(new_filepath) # for the files iterated replace the old name with new names
        print(filepath.name)


#.name gives me full name of files
#.suffix gives me the types of the files